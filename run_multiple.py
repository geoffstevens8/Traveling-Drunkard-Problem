import sys
import optparse

import csv
import knapsack
import tsp_solver
import config
import matplotlib.pyplot as plt
import numpy as np

(r, n, d, u) = knapsack.simulated_annealing_knapsack(dist, tsp)
