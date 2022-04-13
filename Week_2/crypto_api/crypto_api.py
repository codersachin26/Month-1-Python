import json
import logging

import requests

from Week_1.bar_chart.draw_bar_chart import is_list_of


class CryptoApi:
    def get_prices(self,max_days=30, crypto_ids=None):
        """
        get_prices() func, return prices of cryptos as dict.
        """
        endpoint = f"https://api.coingecko.com/api/v3/coins/ID/market_chart?vs_currency=usd&days={max_days}&interval=daily"

        if not is_list_of(str, crypto_ids):
            logging.error(f'get_cryptos_price_data(data: list[str]) get called with wrong data type data: {crypto_ids}')
            return -1

        cryptos = {}

        # hit api for each crypto id
        for crypto_id in crypto_ids:
            label = crypto_id
            prices = []
            api = endpoint.replace('ID', crypto_id)

            try:
                res = requests.get(api)
                logging.debug(f'called api endpoint : {api}')
            except requests.exceptions.RequestException as e:
                logging.error(f'api call failed, Error: {e}')
                return

            if res.status_code == 200:
                logging.debug(f'API response status code: {res.status_code}')
            else:
                logging.error(f'api response status : {res.status_code}')
                return

            try:
                crypto_data = json.loads(res.text)
                logging.debug(f'api response converted into python object ResponseObject: {crypto_data}')
            except json.decoder.JSONDecodeError as err:
                logging.error(f'json.loads() failed to parse response, Error: {repr(err)}')
                return -1

            for price in crypto_data.get('prices'):
                prices.append(price[1])

            cryptos[label] = prices

        return cryptos

    def get_volumes(self,max_cryptos=30):
        """
        get_volumes(), return list of crypto volume data as dict.
        """
        endpoint = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
        try:
            res = requests.get(endpoint)
            logging.debug(f'hit api call endpoint : {endpoint}')
        except requests.exceptions.RequestException as e:
            logging.error(f'api call failed {e}')
            return

        if res.status_code == 200:
            logging.debug(f'API response status code: {res.status_code}')
        else:
            logging.error(f'api response status code : {res.status_code}')
            return

        cryptos = json.loads(res.text)

        cryptos_data = {}

        for i, crypto in enumerate(cryptos):
            crypto_name = crypto.get('name')
            market_cap = crypto.get('market_cap')
            cryptos_data[crypto_name] = market_cap

            if i == max_cryptos:
                break

        return cryptos_data
