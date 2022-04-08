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
from Week_1.pie_chart.draw_pie_chart import API_ENDPOINT
import logging

# logger configuration
LOG_FILE_NAME = "draw_bar_chart.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'



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
    logging.info('start draw_bar_chart function')
    plt.xlabel("Crypto Name")
    plt.ylabel("Volume in Billions")
    plt.title("Top 10 High Crypto Volume Data")
    logging.info('added plotting attributes - xlable, ylable, title ')
    plt.bar(data, label)
    plt.show()
    logging.info('end draw_bar_chart function')


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
    logging.info('start draw_crypto_volume function')
    logging.info(f'call API endpoint : {API_ENDPOINT}')
    res = requests.get(API_ENDPOINT)

    if res.status_code == 200:
        logging.info(f'API response status code: {res.status_code}')
    else:
        logging.error(f'api response status : {res.status_code}')

    cryptos = json.loads(res.text)
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

    logging.info('call draw_bar_chart with labels and volume data')

    draw_bar_chart(labels, volumes)
    logging.info('end draw_crypto_volume function')


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    draw_crypto_volume()
