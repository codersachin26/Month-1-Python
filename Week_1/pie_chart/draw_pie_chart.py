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

import matplotlib.pyplot as plt
import requests
import json

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"


def draw_pie_chart(data, labels):
    """
    draw the pie chart with crypto market cap data.

    Parameters
    ----------
    data : list of int
        cryptos market cap data.

    labels : str
        crypto name

    """
    plt.pie(data, labels=labels, autopct='% 1.1f %%', shadow=True)
    plt.legend(title='Cryptos name')
    plt.title("Cryptos Market Cap in 2022")
    plt.show()


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
    res = requests.get(API_ENDPOINT)
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


if __name__ == "__main__":
    draw_crypto_market_cap()
