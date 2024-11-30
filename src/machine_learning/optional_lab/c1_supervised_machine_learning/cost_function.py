import numpy as np
from matplotlib import pyplot as plt

from src.machine_learning.optional_lab.c1_supervised_machine_learning.lab_utils_uni import plt_intuition, \
    plt_stationary, plt_update_onclick, soup_bowl

# x_train = np.array([1.0, 2.0])
# y_train = np.array([300.0, 500.0])

def computing_cost(x, y, w, b):
    m = x.shape[0]
    cost_sum = 0.0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y_train[i]) ** 2
        cost_sum += cost

    total_cost = (1 / (2 * m)) * cost_sum
    return total_cost


# Cost Function Intuition
# plt_intuition(x_train, y_train)

# Larger Data Set

x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
y_train = np.array([250, 300, 480, 430, 630, 730,])

plt.ion()

plt.close('all')

fig, ax, dyn_items = plt_stationary(x_train, y_train)
updater = plt_update_onclick(fig, ax, x_train, y_train, dyn_items)

soup_bowl()