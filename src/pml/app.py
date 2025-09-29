#!/urs/bin/env python3

import sys

from pml.model import linear_regression as lr
from pml.graphics import plot as plt


import importlib.resources as pkg_resources


def main():
    file = pkg_resources.files("pml.resources").joinpath("02/pizza.txt")
    X, Y = lr.load_data(file)
    loss = lr.loss(X, Y, 0.1)
    print(f"Loss: {loss}")
    plt.plot_data(X, Y)


if __name__ == "__main__":
    main()
    sys.exit(0)
