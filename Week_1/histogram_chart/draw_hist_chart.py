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

import matplotlib.pyplot as plt
import requests
import json

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
    plt.xlabel("Days")
    plt.ylabel("frequency")
    plt.title("Litecoin Price Frequency")
    plt.hist(data, label='Litecoin')
    plt.legend()
    plt.show()


def draw_litecoin_price_data():
    """
    call the API ENDPOINT via requests library, get the response and
    call the draw_hist_chart function for histogram chart.

    """
    res = requests.get(API_ENDPOINT)
    litecoin_data = json.loads(res.text)
    litecoin_data_prices = []

    # storing Litecoin prices
    for price in litecoin_data.get('prices'):
        litecoin_data_prices.append(price[1])

    draw_hist_chart(litecoin_data_prices)


if __name__ == "__main__":
    draw_litecoin_price_data()
