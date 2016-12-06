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
    parser.add_option('--distance',
                    dest = 'dist',
                    type = 'int',
                    default = 10000,
                    help = 'Provide a maximum distance for the bar crawl')
    parser.add_option('--tsp',
                    dest = 'tsp',
                    default = 'greedy',
                    help = 'Select the TSP solver to use: random, greedy, two-opt')
    parser.add_option('--print-url',
                    dest = 'url',
                    default = False,
                    action = 'store_true',
                    help = 'Print the final URL that will put the bars on Google Maps')
    parser.add_option('--graphs',
                    dest = 'graphs',
                    default = False,
                    action = 'store_true',
                    help = 'Show some graphs about the generated results')
    parser.add_option('--temp',
                    dest = 'temp',
                    default = 'temperature1',
                    help = 'Provide a temperature function for the simulated annealing')
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
    temp = tsp.lower()

    # run the simulated annealing algorithm
    (r, n, d, u) = knapsack.simulated_annealing_knapsack(dist, tsp, temp)

    # generate a url for Google Maps
    if options.url:
        url = 'https://www.google.com/maps/dir/'
        for bar in r:
        	string = config.BAR_LIST[bar][1].replace(' ', '+')
        	url += string + '/'
        url += 'data=!4m2!4m1!3e0' #'data=!4m2!4m1!3e2'

    # display graphs if requested
    if options.graphs:

        '''
        UNCOMMENT TO SEE INDIVIDUAL SPECIFIC PLOTS

        fig, ax1 = plt.subplots()
        ax1.plot(d, 'b-')
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Distance', color='b')
        for tl in ax1.get_yticklabels():
            tl.set_color('b')

        ax2 = ax1.twinx()
        ax2.plot(u, 'r-')
        ax2.set_ylabel('Utility', color='r')
        for tl in ax2.get_yticklabels():
            tl.set_color('r')
        plt.show(1)

        plt.figure(2)
        plt.plot(d)
        plt.xlabel('Iteration')
        plt.ylabel('Distance of Crawl')
        plt.show(2)

        plt.figure(3)
        plt.plot(u)
        plt.xlabel('Iteration')
        plt.ylabel('Utility of Crawl')
        plt.show(3)
        '''

        # combines all graphs into one window
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 12), tight_layout=True)
        ax[0,0].plot(d, color='r')
        ax[0,0].set_title('Distance')
        ax[0,1].plot(u, color='g')
        ax[0,1].set_title('Utility')
        ax[1,0].plot(n, color='k')
        ax[1,0].set_title('Number of Bars in Crawl')
        ax[1,1].plot([a/b for a,b in zip(u,n)])
        ax[1,1].set_title('Utility per Bar')
        plt.show()

    # display essential information after the program has run
    print('\n')
    print('***********************************************')
    print('\n')
    print('SPECIFICATIONS')
    print('Maximum distance: ' + str(dist))
    print('TSP Solver: ' + tsp)
    print('Temperature Function: ' + temp)
    print('\n')
    print('RESULTS')
    print('Final bar crawl: ' + str(r))
    print('Utility: ' + str(u[-1]))
    print('\n')
    if options.url:
        print('Visit this url to see your crawl: ' + url)
        print('\n')

    print('***********************************************')
