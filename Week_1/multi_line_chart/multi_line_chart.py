"""
 Visualize Crypto price data by using multi line chart.

 There are Two functions:
                1. draw_multi_line_chart:
                        this function plot the multi line chart using matplotlib.

                2. get_cryptos_price_data:
                        this function hit the API ENDPOINT for each crypto and
                        return all crypto price data.

 @author: sachin@codeops.tech
"""
import logging
import matplotlib.pyplot as plt
import requests
import json


# logger configuration
from Week_1.bar_chart.draw_bar_chart import is_list_of

LOG_FILE_NAME = "multi_line_chart.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'


API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/ID/market_chart?vs_currency=usd&days=100&interval=daily"


def draw_multi_line_chart():
    """
    get all cryptos price data via calling get_cryptos_price_data function and
    plot multi line chart using matplotlib.

    """

    logging.info('start draw_multi_line_chart() func')
    crypto_ids = ['bitcoin-cash', 'cardano', 'ripple', 'solana', 'terra-luna', 'litecoin']
    cryptos_data = get_cryptos_price_data(crypto_ids)
    if cryptos_data == -1:
        logging.error('get_cryptos_price_data() func call failed, return -1')
        return

    logging.debug(f'get_cryptos_price_data() func get executed, return : {cryptos_data}')

    for label, price in cryptos_data.items():
        plt.plot(price, label=label)

    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.title("Multi Line Charts")
    plt.legend(title='Coins Name')
    plt.show()
    logging.info('end draw_multi_line_chart() func call')


def get_cryptos_price_data(crypto_ids):
    """
    make api calls for each crypto ids, store it and return cryptos' data.

    Parameters
    ----------
    crypto_ids : list of str
        e.g. crypto_ids = ['bitcoin-cash','solana', 'terra-luna', 'litecoin']
        cryptos id name.

    Returns
    -------
    dict : cryptos price data with labels

    """
    logging.info('start get_cryptos_price_data() func')

    if not is_list_of(str, crypto_ids):
        logging.error(f'get_cryptos_price_data(data: list[str]) get called with wrong data type data: {crypto_ids}')
        return -1

    cryptos = {}

    # hit api for each crypto id
    for crypto_id in crypto_ids:
        label = crypto_id
        prices = []
        api = API_ENDPOINT.replace('ID', crypto_id)

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


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    draw_multi_line_chart()
