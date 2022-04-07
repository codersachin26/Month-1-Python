import matplotlib.pyplot as plt
import numpy as np
import requests
import json
from Week_1.pie_chart.draw_pie_chart import API_ENDPOINT


def draw_bar_chart(data, label):
    plt.xlabel("Crypto Name")
    plt.ylabel("Volume")
    plt.bar(data, label)
    plt.show()


def draw_crypto_volume(size=10):
    res = requests.get(API_ENDPOINT)
    cryptos = json.loads(res.text)
    labels = []
    volumes = []

    for i, crypto in enumerate(cryptos):
        crypto_name = crypto.get('name')
        volume = crypto.get('total_volume')
        labels.append(crypto_name)
        volumes.append(volume)

        if i == size:
            break

    draw_bar_chart(np.array(labels), np.array(volumes))


if __name__ == "__main__":
    draw_crypto_volume()
