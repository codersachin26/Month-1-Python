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

import matplotlib.pyplot as plt
import requests
import json

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

    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.plot(data)
    plt.legend(title='Bitcoin')
    plt.show()


def draw_btc_price_data():
    """
    call the API ENDPOINT via requests library, get the response and
    call the draw_line_chart function with response data.

    """
    res = requests.get(API_ENDPOINT)
    btc_data = json.loads(res.text)
    print(json.dumps(btc_data))
    btc_prices = []

    for price in btc_data.get('prices'):
        btc_prices.append(price[1])

    draw_line_chart(btc_prices)


if __name__ == "__main__":
    draw_btc_price_data()
