import matplotlib.pyplot as plt
import requests
import json

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"


def draw_pie_chart(data, labels, title):
    plt.pie(data, labels=labels, autopct='% 1.1f %%', shadow=True)
    plt.legend(title=title)
    plt.show()


def draw_crypto_market_cap(size=7):
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

    draw_pie_chart(market_caps,  labels, 'Cryptos Market Cap')


if __name__ == "__main__":
    draw_crypto_market_cap()
