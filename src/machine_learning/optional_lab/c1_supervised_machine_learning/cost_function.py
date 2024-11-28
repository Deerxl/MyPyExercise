import numpy as np

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

def computing_cost(x, y, w, b):
    m = x.shape[0]