"""
 Visualize Crypto market cap data by using pie chart.

 There are Two functions:
                1. draw_pie_chart:
                        this function plot the pie chart using matplotlib.

                2. draw_crypto_market_cap:
                        this function hit the API ENDPOINT,
                        parse the response and call the draw_pie_chart() function.

 @author: sachin@codeops.tech
"""
import logging
import matplotlib.pyplot as plt
import requests
import json

# logger configuration
from Week_1.bar_chart.draw_bar_chart import is_list_of

LOG_FILE_NAME = "draw_pie_chart.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"


def draw_pie_chart(data, labels):
    """
    draw the pie chart with crypto market cap data.

    Parameters
    ----------
    data : list of int
        cryptos market cap data.

    labels : list of str
        crypto name

    """

    if not is_list_of(int, data) or not is_list_of(str, labels):
        logging.error(f'draw_pie_chart(data: list[int],labels: list[str]) get called with wrong data type data: {data}, label: {labels}')
        return -1

    plt.pie(data, labels=labels, autopct='% 1.1f %%', shadow=True)
    plt.legend(title='Cryptos name')
    plt.title("Cryptos Market Cap in 2022")
    plt.show()

    logging.info('end draw_pie_chart() func')


def draw_crypto_market_cap(size=7):
    """
    call the API ENDPOINT via requests library and
    call the draw_pie_chart function for pie chart.

    Parameters
    ----------
    size : int
        default -> 7
        how many cryptos currencies should be plotted.

    Returns
    -------
    None

    """

    try:
        res = requests.get(API_ENDPOINT)
        logging.debug(f'hit api call endpoint : {API_ENDPOINT}')
    except requests.exceptions.RequestException as e:
        logging.error(f'api call failed {e}')
        return

    if res.status_code == 200:
        logging.debug(f'API response status code: {res.status_code}')
    else:
        logging.error(f'api response status code : {res.status_code}')
        return

    cryptos = json.loads(res.text)
    labels = []
    market_caps = []

    for i, crypto in enumerate(cryptos):
        crypto_name = crypto.get('name')
        market_cap = crypto.get('market_cap')
        labels.append(crypto_name)
        market_caps.append(market_cap)

        if i == size:
            break

    draw_pie_chart(market_caps,  labels)
    logging.info('end draw_crypto_market_cap() func')


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    draw_crypto_market_cap()
