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
    for i in range(1):
        (r, n, d, u) = knapsack.simulated_annealing_knapsack(dist, tsp)
        us.append(u[-1])
        ds.append(d[-1])
        ns.append(n[-1])
    all_tsps_u.append(us)
    all_tsps_d.append(ds)
    all_tsps_n.append(ns)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

random_plot, = ax[0,0].plot(all_tsps_u[0], label='random')
greedy_plot, = ax[0,0].plot(all_tsps_u[1], label='greedy')
twoopt_plot, = ax[0,0].plot(all_tsps_u[2], label='twoopt')
sa_plot, = ax[0,0].plot(all_tsps_u[3], label='sa')
ax[0,0].set_title('Utility')

random_plot2, = ax[0,1].plot(all_tsps_d[0], label='random')
greedy_plot2, = ax[0,1].plot(all_tsps_d[1], label='greedy')
twoopt_plot2, = ax[0,1].plot(all_tsps_d[2], label='twoopt')
sa_plot2, = ax[0,1].plot(all_tsps_d[3], label='sa')

random_plot, = ax[1,0].plot(all_tsps_n[0], label='random')
greedy_plot, = ax[1,0].plot(all_tsps_n[1], label='greedy')
twoopt_plot, = ax[1,0].plot(all_tsps_n[2], label='twoopt')
sa_plot, = ax[1,0].plot(all_tsps_n[3], label='sa')

fig.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'], 'upper left')
plt.show()

'''
UNCOMMENT FOR INDIVIDUAL PLOTS

plt.figure()
random_plot, = plt.plot(all_tsps_u[0], label='random')
greedy_plot, = plt.plot(all_tsps_u[1], label='greedy')
twoopt_plot, = plt.plot(all_tsps_u[2], label='twoopt')
sa_plot, = plt.plot(all_tsps_u[3], label='sa')
plt.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

plt.figure()
random_plot, = plt.plot(all_tsps_d[0], label='random')
greedy_plot, = plt.plot(all_tsps_d[1], label='greedy')
twoopt_plot, = plt.plot(all_tsps_d[2], label='twoopt')
sa_plot, = plt.plot(all_tsps_d[3], label='sa')
plt.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

plt.figure()
random_plot, = plt.plot(all_tsps_n[0], label='random')
greedy_plot, = plt.plot(all_tsps_n[1], label='greedy')
twoopt_plot, = plt.plot(all_tsps_n[2], label='twoopt')
sa_plot, = plt.plot(all_tsps_n[3], label='sa')
plt.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
'''
