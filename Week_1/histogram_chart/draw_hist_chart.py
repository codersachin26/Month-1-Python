import matplotlib.pyplot as plt
import requests
import json

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=100&interval=daily"


def draw_hist_chart(data):
    plt.xlabel("Days")
    plt.ylabel("frequency")
    plt.title("Litecoin Frequency")
    plt.hist(data, label='Litecoin')
    plt.legend()
    plt.show()


def draw_litecoin_price_data():
    res = requests.get(API_ENDPOINT)
    litecoin_data = json.loads(res.text)
    litecoin_data_prices = []

    for price in litecoin_data.get('prices'):
        litecoin_data_prices.append(price[1])

    draw_hist_chart(litecoin_data_prices)


if __name__ == "__main__":
    draw_litecoin_price_data()
