"""
 Visualize Crypto volume data by using bar chart.

 There are Two functions:
                1. draw_bar_chart:
                        this function plot the BAR graph.

                2. draw_crypto_volume:
                        this function hit the API ENDPOINT,
                         parse the data and call the draw_bar_chart() function.

 @author: sachin@codeops.tech
"""

import matplotlib.pyplot as plt
import requests
import json
import logging


API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"


# logger configuration
LOG_FILE_NAME = "draw_bar_chart.log"
LEVEL = logging.DEBUG
FORMAT = '[%(asctime)s] : %(levelname)s -> %(message)s'


# check type of list elements
def is_list_of(element_type, list_elements):
    for list_element in list_elements:
        if not isinstance(list_element, element_type):
            return False
    else:
        return True


def draw_bar_chart(data, label):
    """
    draw the bar chart by using data & label args

    Parameters
    ----------
    data : list of int
        e.g. data = [1233,3673,3333,979784,5754,45757,443433]
        cryptos volume data.

    label : list of str
        e.g. label = ['bitcoin', 'cardano', 'ripple', 'solana','litecoin']
        cryptos names for labels.

    Returns
    -------
    None

    """

    if not is_list_of(int, data) or not is_list_of(str, label):
        logging.error(f'draw_bar_chart() get called with wrong data type data: {data}, label: {label}')
        return -1

    plt.xlabel("Crypto Name")
    plt.ylabel("Volume in Billions")
    plt.title("Top 10 High Crypto Volume Data")
    plt.bar(label, data)
    plt.show()

    logging.debug('draw_bar_chart() function, successfully draw bar chart')
    logging.debug('end draw_bar_chart() function')


def draw_crypto_volume(size=10):
    """
    main function of this module.
    call the API ENDPOINT via requests library and
    call the draw_bar_chart function for bar chart.

    Parameters
    ----------
    size : int
        default -> 10
        how many cryptos currencies should be plotted.


    Returns
    -------
    None

    """

    if not isinstance(size, int):
        logging.error(
            f'draw_crypto_volume(size: int) get called with wrong data type, expected size: int but got {type(size)}')
        return

    logging.debug(f'draw_crypto_volume() get called with size: {size}')
    logging.debug(f'call API endpoint : {API_ENDPOINT}')

    try:
        res = requests.get(API_ENDPOINT)
    except requests.exceptions.RequestException as e:
        logging.error(f'api call failed {e}')
        return

    if res.status_code == 200:
        logging.debug(f'API response status code: {res.status_code}')
    else:
        logging.debug(f'api response status : {res.status_code}')
        return

    logging.debug(f'api response Json: {res.text}')

    try:
        cryptos = json.loads(res.text)
        logging.debug(f'api response converted into python object ResponseObject: {cryptos}')
    except json.decoder.JSONDecodeError as err:
        logging.error(f'json.loads() failed to parse response, Error: {repr(err)}')
        return -1

    labels = []
    volumes = []

    # store labels & volumes from api response
    for i, crypto in enumerate(cryptos):
        crypto_name = crypto.get('name')
        volume = crypto.get('total_volume')
        labels.append(crypto_name)
        volumes.append(volume)

        if i == size:
            break

    draw_bar_chart(volumes, labels)
    logging.info('draw_crypto_volume() func, successfully executed')


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    draw_crypto_volume()
