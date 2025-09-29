#!/urs/bin/env python3

import sys

from pml.regression import linear as lr
from pml.graphics import plot as plt

import importlib.resources as pkg_resources


def main():
    file = pkg_resources.files("pml.resources").joinpath("02/pizza.txt")
    X, Y = lr.load_data(file)
    plt.plot_data(X, Y)

if __name__ == "__main__":
    main()
    sys.exit(0)
