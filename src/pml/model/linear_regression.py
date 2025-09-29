import numpy as np



def load_data(file_name):
    X, Y = np.loadtxt(file_name, skiprows=1, unpack=True)
    return X, Y

def predict(X, w):
    return X * w

def loss(X, Y, w):
    Y_pred = predict(X, w)
    return ((Y_pred - Y) ** 2).mean()

def train(X, Y, epochs=1000, lr):
    w = 0
    for i in range(epochs):
        current_loss = loss(X, Y, w)
        print("Iteration %4d => Loss: %.6f" % (i, current_loss))

        if loss(X, Y, w + lr) < current_loss:
            w += lr
        elif loss(X, Y, w - lr) < current_loss:
            w -= lr
        else:
            return w
    raise Exception("Couldn't converge within %d epochs" % epochs)
