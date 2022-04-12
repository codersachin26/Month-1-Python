"""
 Visualize Crypto price data by using line chart.

 There are Two functions:
                1. draw_line_chart:
                        this function plot the line chart using matplotlib.

                2. draw_btc_price_data:
                        this function hit the API ENDPOINT,
                        parse the response and call the draw_line_chart() function.

 @author: sachin@codeops.tech
"""
import logging

import matplotlib.pyplot as plt
import requests
import json
from Week_1.bar_chart.draw_bar_chart import is_list_of


# logger configuration
LOG_FILE_NAME = "draw_line_chart.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=100&interval=daily"


def draw_line_chart(data):
    """
    draw the line chart by using crypto price data.

    Parameters
    ----------
    data : list of int
        e.g. data = [1233,3673,3333,979784,5754,45757,443433]
        cryptos price data.

    """

    if not is_list_of(float, data):
        logging.error(f'draw_line_chart(data: list[float]) get called with wrong data type data: {data}')
        return -1

    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.plot(data)
    plt.legend(title='Bitcoin')
    plt.show()
    logging.info('end draw_line_chart function')


def draw_btc_price_data():
    """
    call the API ENDPOINT via requests library, get the response and
    call the draw_line_chart function with response data.

    """

    logging.info('start draw_btc_price_data function')
    logging.info(f'call API endpoint : {API_ENDPOINT}')

    try:
        res = requests.get(API_ENDPOINT)
    except requests.exceptions.RequestException as e:
        logging.error(f'api call failed {e}')
        return

    try:
        btc_data = json.loads(res.text)
        logging.debug(f'api response converted into python object ResponseObject: {btc_data}')
    except json.decoder.JSONDecodeError as err:
        logging.error(f'json.loads() failed to parse response, Error: {repr(err)}')
        return -1

    btc_prices = []

    if res.status_code == 200:
        logging.debug(f'API response status code: {res.status_code}')
    else:
        logging.error(f'api response status code: {res.status_code}')

    for price in btc_data.get('prices'):
        btc_prices.append(price[1])

    draw_line_chart(btc_prices)
    logging.debug('called draw_line_chart with btc_prices')
    logging.info('end draw_btc_price_data function')


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    draw_btc_price_data()
