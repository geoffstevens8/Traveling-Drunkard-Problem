import sys
import optparse

import csv
import knapsack
import tsp_solver
import config
import matplotlib.pyplot as plt
import numpy as np

def readCommand(argv):
    parser = optparse.OptionParser(description = 'Run public tests on student code')
    parser.set_defaults(generateSolutions=False, edxOutput=False, muteOutput=False, printTestCase=False, noGraphics=False)
    parser.add_option('--distance',
                      dest = 'dist',
                      type = 'int',
                      default = 10000,
                      help = 'Provide a maximum distance for the bar crawl')
    parser.add_option('--tsp',
                      dest = 'tsp',
                      default = 'greedy',
                      help = 'Select the TSP solver to use: greedy, two-opt')
    (options, args) = parser.parse_args(argv)
    return options

if __name__ == '__main__':
    options = readCommand(sys.argv)

    dist = options.dist
    tsp = options.tsp
    tsp = tsp.lower()
    print(tsp)
    (r, d, u) = knapsack.simulated_annealing_knapsack(dist, tsp)

    print(r)
