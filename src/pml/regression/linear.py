import numpy as np



def load_data(file_name):
    X, Y = np.loadtxt(file_name, skiprows=1, unpack=True)
    return X, Y