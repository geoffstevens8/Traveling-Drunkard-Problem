import sys
import optparse

import csv
import knapsack
import tsp_solver
import config
import matplotlib.pyplot as plt
import numpy as np

def readCommand(argv):
    parser = optparse.OptionParser(description = 'Run code')
    parser.add_option('--distance',
                    dest = 'dist',
                    type = 'int',
                    default = 10000,
                    help = 'Provide a maximum distance for the bar crawl')
    parser.add_option('--iterations',
                    dest = 'iterations',
                    type = 'int',
                    default = 3,
                    help = 'Provide the number of times to find a solution for each tsp')
    parser.add_option('--tsp',
                    dest = 'tsp',
                    default = 'greedy',
                    help = 'Select the TSP solver to use: random, greedy, two-opt')
    parser.add_option('--graphs',
                    dest = 'graphs',
                    default = False,
                    action = 'store_true',
                    help = 'Show some graphs about the generated results')
    parser.add_option('--temp',
                    dest = 'temp',
                    default = 'simple',
                    help = 'Provide a temperature function for the simulated annealing')
    parser.add_option('--length',
                    dest = 'length',
                    type = 'int',
                    default = -1,
                    help = 'Provide a maximum to the number of bars in the crawl')
    (options, args) = parser.parse_args(argv)
    return options

if __name__ == '__main__':

    # read in the command line arguments
    options = readCommand(sys.argv)

    # assign variables based on input
    dist = options.dist
    tsp = options.tsp
    tsp = tsp.lower()
    temp = options.temp
    temp = temp.lower()
    iterations = options.iterations
    if options.length == -1:
        length = None
    else:
        length = int(options.length)

    tsps = ['random', 'greedy', 'two-opt', 'sa']

    all_tsps_u = []
    all_tsps_d = []
    all_tsps_n = []

    for tsp in tsps:
        us = []
        ds = []
        ns = []
        for i in range(iterations):
            (r, n, d, u) = knapsack.simulated_annealing_knapsack(dist, tsp, temperature=temp, bar_limit=length)
            us.append(u[-1])
            ds.append(d[-1])
            ns.append(n[-1])
        all_tsps_u.append(us)
        all_tsps_d.append(ds)
        all_tsps_n.append(ns)

    if options.graphs:

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
        ax[0,1].set_title('Distance of Bar Crawl')

        random_plot3, = ax[1,0].plot(all_tsps_n[0], label='random')
        greedy_plot3, = ax[1,0].plot(all_tsps_n[1], label='greedy')
        twoopt_plot3, = ax[1,0].plot(all_tsps_n[2], label='twoopt')
        sa_plot3, = ax[1,0].plot(all_tsps_n[3], label='sa')
        ax[1,0].set_title('Number of Bars')

        random_plot4, = ax[1,1].plot([a/b for a,b in zip(all_tsps_u[0], all_tsps_n[0])], label='random')
        greedy_plot4, = ax[1,1].plot([a/b for a,b in zip(all_tsps_u[1], all_tsps_n[1])], label='greedy')
        twoopt_plot4, = ax[1,1].plot([a/b for a,b in zip(all_tsps_u[2], all_tsps_n[2])], label='twoopt')
        sa_plot4, = ax[1,1].plot([a/b for a,b in zip(all_tsps_u[3], all_tsps_n[3])], label='sa')
        ax[1,1].set_title('Utility per Bar')

        fig.legend([random_plot, greedy_plot, twoopt_plot, sa_plot], ['Random', 'Greedy', 'Two-Opt', 'SA'], 'upper left')
        plt.show()

        print('\n')
        print('***********************************************')
        print('\n')
        print('SPECIFICATIONS')
        print('Maximum distance: ' + str(dist))
        print('Iterations: ' + str(iterations))
        print('Temperature Function: ' + temp)
        print('Maximum Number of Bars: ' + str(length))
        print('\n')
        print('RESULTS')
        print('Average Utility')
        print('Random: ' + str( sum(all_tsps_u[0]) / float(iterations)) )
        print('Greedy: ' + str( sum(all_tsps_u[1]) / float(iterations)) )
        print('Two-opt: ' + str( sum(all_tsps_u[2]) / float(iterations)) )
        print('Simulated Annealing: ' + str( sum(all_tsps_u[3]) / float(iterations)) )
        print('\n')
        print('Average Distance')
        print('Random: ' + str( sum(all_tsps_d[0]) / float(iterations)) )
        print('Greedy: ' + str( sum(all_tsps_d[1]) / float(iterations)) )
        print('Two-opt: ' + str( sum(all_tsps_d[2]) / float(iterations)) )
        print('Simulated Annealing: ' + str( sum(all_tsps_d[3]) / float(iterations)) )
        print('\n')
        print('Average Number of Bars')
        print('Random: ' + str( sum(all_tsps_n[0]) / float(iterations)) )
        print('Greedy: ' + str( sum(all_tsps_n[1]) / float(iterations)) )
        print('Two-opt: ' + str( sum(all_tsps_n[2]) / float(iterations)) )
        print('Simulated Annealing: ' + str( sum(all_tsps_n[3]) / float(iterations)) )
        print('\n')

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
