"""
 Visualize Crypto Frequency data by using histogram chart.

 There are Two functions:
                1. draw_hist_chart:
                        this function plot the histogram graph.

                2. draw_litecoin_price_data:
                        this function hit the API ENDPOINT,
                        parse the response and call the draw_hist_chart() function.

 @author: sachin@codeops.tech
"""
import logging

import matplotlib.pyplot as plt
import requests
import json


# logger configuration
LOG_FILE_NAME = "draw_hist_chart.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'

# crypto api endpoint
API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=100&interval=daily"


def draw_hist_chart(data):
    """
    draw the histogram chart through crypto price data

    Parameters
    ----------
    data : list of int
        e.g. data = [1233,3673,3333,979784,5754,45757,443433]
        crypto price data.

    """
    logging.info('start draw_hist_chart function')
    plt.xlabel("Days")
    plt.ylabel("frequency")
    plt.title("Litecoin Price Frequency")
    plt.hist(data, label='Litecoin')
    plt.legend()
    plt.show()
    logging.info('end draw_hist_chart function')


def draw_litecoin_price_data():
    """
    call the API ENDPOINT via requests library, get the response and
    call the draw_hist_chart function for histogram chart.

    """
    logging.info('start draw_litecoin_price_data function')
    logging.info(f'call API endpoint : {API_ENDPOINT}')
    res = requests.get(API_ENDPOINT)
    litecoin_data = json.loads(res.text)
    litecoin_data_prices = []

    if res.status_code == 200:
        logging.info(f'API response status code: {res.status_code}')
    else:
        logging.error(f'api response status : {res.status_code}')

    # storing Litecoin prices
    for price in litecoin_data.get('prices'):
        litecoin_data_prices.append(price[1])

    draw_hist_chart(litecoin_data_prices)
    logging.info('call draw_hist_chart with litecoin_data_prices')
    logging.info('end draw_litecoin_price_data function')


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    draw_litecoin_price_data()
