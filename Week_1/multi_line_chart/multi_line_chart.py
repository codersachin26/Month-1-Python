import matplotlib.pyplot as plt
import requests
import json

API_ENDPOINT = "https://api.coingecko.com/api/v3/coins/ID/market_chart?vs_currency=usd&days=100&interval=daily"


def draw_multi_line_chart():
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
    cryptos = {}

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
