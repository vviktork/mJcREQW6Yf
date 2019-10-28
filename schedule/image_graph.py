# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from io import BytesIO
import base64


def image_graph(data):
    plt.figure(figsize=(10, 10))
    plt.plot(data[0], data[1], color='orange', )
    plt.scatter(data[0], data[1], color='orange', )
    if len(data[0]) > 8: plt.xticks(rotation=60)
    plt.grid(axis='y')
    image = BytesIO()
    plt.savefig(image,  format="PNG")
    images = base64.b64encode(image.getvalue()).decode('utf-8')
    return images