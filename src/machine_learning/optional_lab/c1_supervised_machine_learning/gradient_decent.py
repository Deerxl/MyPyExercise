import copy
import math

import numpy as np
from matplotlib import pyplot as plt
plt.style.use('./deeplearning.mplstyle')

from src.machine_learning.optional_lab.c1_supervised_machine_learning.lab_utils_uni import plt_gradients, \
    plt_contour_wgrad, plt_divergence

# Load our data set

x_train = np.array([1.0, 2.0])   #features
y_train = np.array([300.0, 500.0])   #target value


def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0

    for i in range(m):
        f_wb = w * x[i] + b
        cost += (f_wb - y[i]) ** 2

    total_cost = (1 / (2 * m)) * cost

    return total_cost


def compute_gradient(x, y, w, b):
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = w * x[i] + b
        dj_dw += (f_wb - y[i]) * x[i]
        dj_db += f_wb - y[i]

    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_dw, dj_db


plt_gradients(x_train,y_train, compute_cost, compute_gradient)
plt.show()


def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function):
    """
    Performs gradient descent to fit w,b. Updates w,b by taking
    num_iters gradient steps with learning rate alpha

    Args:
      :param x: (ndarray (m,))  : Data, m examples
      :param y: (ndarray (m,))  : target values
      :param w_in: (scalar): initial values of model parameters
      :param b_in: (scalar): initial values of model parameters
      :param alpha: (float):     Learning rate
      :param num_iters: (int):   number of iterations to run gradient descent
      :param cost_function:     function to call to produce cost
      :param gradient_function: function to call to produce gradient

    Returns:
      w (scalar): Updated value of parameter after running gradient descent
      b (scalar): Updated value of parameter after running gradient descent
      J_history (List): History of cost values
      p_history (list): History of parameters [w,b]
    """

    w = copy.deepcopy(w_in)
    b = copy.deepcopy(b_in)

    j_history = []
    p_history = []

    for i in range(num_iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)

        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        if i < 100000:
            j_history.append(cost_function(x, y, w, b))
            p_history.append([w, b])

        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4}: Cost {j_history[-1]:0.2e} ",
                  f"dj_dw: {dj_dw:0.3e}, dj_db: {dj_db:0.3e} ",
                  f"w: {w:0.3e}, b: {b:0.5e}")

    return w, b, j_history, p_history


w_init = 0
b_init = 0

iterations = 10000
tmp_alpha = 1.0e-2

w_final, b_final, J_hist, p_hist = gradient_descent(x_train, y_train, w_init, b_init, tmp_alpha, iterations,
                                                          compute_cost, compute_gradient)

print(f"(w, b) found by gradient descent: ({w_final:8.4f}, {b_final:8.4f})")


# plot cost versus iteration
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, figsize=(12,4))
ax1.plot(J_hist[:100])
ax2.plot(1000 + np.arange(len(J_hist[1000:])), J_hist[1000:])
ax1.set_title("Cost vs. iteration(start)");  ax2.set_title("Cost vs. iteration (end)")
ax1.set_ylabel('Cost')            ;  ax2.set_ylabel('Cost')
ax1.set_xlabel('iteration step')  ;  ax2.set_xlabel('iteration step')
plt.show()


# predictions
print(f"1000 sqft house prediction {w_final*1.0 + b_final:0.1f} Thousand dollars")
print(f"1200 sqft house prediction {w_final*1.2 + b_final:0.1f} Thousand dollars")
print(f"2000 sqft house prediction {w_final*2.0 + b_final:0.1f} Thousand dollars")


fig, ax = plt.subplots(1,1, figsize=(12, 6))
plt_contour_wgrad(x_train, y_train, p_hist, ax)


fig, ax = plt.subplots(1,1, figsize=(12, 4))
plt_contour_wgrad(x_train, y_train, p_hist, ax, w_range=[180, 220, 0.5], b_range=[80, 120, 0.5],
            contours=[1,5,10,20],resolution=0.5)


# increase the learning rate

# initialize parameters
w_init = 0
b_init = 0

# set alpha to a large value
iterations = 10
tmp_alpha = 8.0e-1

# run gradient descent
w_final, b_final, J_hist, p_hist = gradient_descent(x_train ,y_train, w_init, b_init, tmp_alpha,
                                                    iterations, compute_cost, compute_gradient)


plt_divergence(p_hist, J_hist,x_train, y_train)
plt.show()