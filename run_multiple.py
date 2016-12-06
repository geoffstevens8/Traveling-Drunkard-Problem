import sys
import optparse

import csv
import knapsack
import tsp_solver
import config
import matplotlib.pyplot as plt
import numpy as np


dist = 20000
tsps = ['random', 'greedy', 'two-opt', 'sa']

all_tsps_u = []
all_tsps_d = []
all_tsps_n = []

for tsp in tsps:
    us = []
    ds = []
    ns = []
    for i in range(2):
        (r, n, d, u) = knapsack.simulated_annealing_knapsack(dist, tsp)
        us.append(u[-1])
        ds.append(d[-1])
        ns.append(n[-1])
    all_tsps_u.append(us)
    all_tsps_d.append(ds)
    all_tsps_n.append(ns)

plt.figure()
random_plot, = plt.plot(all_tsps_u[0], label='random')
greedy_plot, = plt.plot(all_tsps_u[1], label='greedy')
twoopt_plot, = plt.plot(all_tsps_u[2], label='twoopt')
sa_plot, = plt.plot(all_tsps_u[3], label='sa')
plt.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'])
plt.show()

plt.figure()
random_plot, = plt.plot(all_tsps_d[0], label='random')
greedy_plot, = plt.plot(all_tsps_d[1], label='greedy')
twoopt_plot, = plt.plot(all_tsps_d[2], label='twoopt')
sa_plot, = plt.plot(all_tsps_d[3], label='sa')
plt.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'])
plt.show()

plt.figure()
random_plot, = plt.plot(all_tsps_n[0], label='random')
greedy_plot, = plt.plot(all_tsps_n[1], label='greedy')
twoopt_plot, = plt.plot(all_tsps_n[2], label='twoopt')
sa_plot, = plt.plot(all_tsps_n[3], label='sa')
plt.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'])
plt.show()
