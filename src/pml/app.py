#!/urs/bin/env python3

import sys

from pml.model import linear_regression as model
from pml.graphics import plot as plt


import importlib.resources as pkg_resources


def main():
    file = pkg_resources.files("pml.resources").joinpath("02/pizza.txt")
    X, Y = model.load_data(file)

    w = model.train(X, Y, epochs=1000, lr=0.01)
    print("\nw: %.2f" % w)
    # plt.plot_data(X, Y)

    print("Prediction: x=%d => y=%.2f" % (20, model.predict(20, w)))


if __name__ == "__main__":
    main()
    sys.exit(0)
