import sys
import optparse

import csv
import knapsack
import tsp_solver
import config
import matplotlib.pyplot as plt
import numpy as np


dist = 20000
tsps = ['random', 'greedy', 'two-opt']

all_tsps = []

for tsp in tsps:
    curr = []
    for i in range(10):
        (r, n, d, u) = knapsack.simulated_annealing_knapsack(dist, tsp)
        curr.append(u[-1])
    all_tsps.append(curr)

plt.figure()
random_plot, = plt.plot(all_tsps[0], label='random')
greedy_plot, = plt.plot(all_tsps[1], label='greedy')
twoopt_plot, = plt.plot(all_tsps[2], label='twoopt')
plt.legend([random_plot, greedy_plot, twoopt_plot], ['Random', 'Greedy', 'Two-Opt'])
plt.show()
