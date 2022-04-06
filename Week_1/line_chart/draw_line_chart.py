import matplotlib.pyplot as plt
import numpy as np
import requests
import json

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=50&interval=daily"


def draw_line_chart(data):
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.plot(data)
    plt.legend(title='Bitcoin')
    plt.show()


def draw_btc_price_data():
    res = requests.get(API_ENDPOINT)
    btc_data = json.loads(res.text)
    btc_prices = []

    for price in btc_data.get('prices'):
        btc_prices.append(price[1])

    draw_line_chart(np.array(btc_prices))



if __name__ == "__main__":
    draw_btc_price_data()

