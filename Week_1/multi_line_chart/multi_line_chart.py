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

import matplotlib.pyplot as plt
import requests
import json

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/ID/market_chart?vs_currency=usd&days=100&interval=daily"


def draw_multi_line_chart():
    """
    get all cryptos price data via calling get_cryptos_price_data function and
    plot multi line chart using matplotlib.

    """
    crypto_ids = ['bitcoin-cash', 'cardano', 'ripple', 'solana', 'terra-luna', 'litecoin']
    cryptos_data = get_cryptos_price_data(crypto_ids)

    for label, price in cryptos_data.items():
        plt.plot(price, label=label)

    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.title("Multi Line Charts")
    plt.legend(title='Coins Name')
    plt.show()


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

    cryptos = {}

    # hit api for each crypto id
    for crypto_id in crypto_ids:
        label = crypto_id
        prices = []
        api = API_ENDPOINT.replace('ID', crypto_id)
        res = requests.get(api)
        crypto_data = json.loads(res.text)

        for price in crypto_data.get('prices'):
            prices.append(price[1])

        cryptos[label] = prices

    return cryptos


if __name__ == "__main__":
    draw_multi_line_chart()
