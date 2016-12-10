'''

Inputs:
Takes in a maximum distance that will be the constraint.

Outputs:
Final list of bars in order that they should be traveled

'''

import tsp_solver
import random
import copy
import csv
import sys
from math import exp

import config
config.init()

''' KNAPSACK INITIALIZATION '''
def initialize_knapsack():
    # select one bar, return
    # return all bars not in knapsack

    # empty knapsack
    knapsack = []

    # number of bars and list of all indices
    num_bars = len(config.BAR_LIST)

    # add random first bar to knapsack
    first = random.randint(0,num_bars-1)
    knapsack.append(first)

    # build the list of bars not in the knapsack
    not_knapsack = [x for x in range(num_bars)]
    not_knapsack.remove(first)

    return (knapsack, not_knapsack)

''' BAR UTILITY '''
def bar_utility1(bar):
    # some function of cost and stars
    stars = config.BAR_LIST[bar][2]
    dollars = len(config.BAR_LIST[bar][3])

    # utility function of stars and dollars
    utility = float(stars) + (5 - dollars)

    return utility

''' KNAPSACK UTILITY '''
def knapsack_utility(knapsack, utility):
    # determine the utility of the knapsack with a
    # utility function for each bar
    total_utility = 0

    for bar in knapsack:
        total_utility += utility(bar)

    return total_utility

''' TEMPERATURE FUNCTION '''
def simple(index, difference):
    return (1./(index+2)) #+ (1./(difference+.0001))

def kirkpatrick(index, difference):
    current_temp = 1e10 * 0.95**(index)
    return exp(-difference/current_temp)


''' MUTATE KNAPSACK FUNCTIONS '''
def add(knapsack, not_knapsack):
    if len(not_knapsack) < 1:
        return knapsack, not_knapsack
    else:
        selection = random.randint(0, len(not_knapsack)-1)
        to_add = not_knapsack[selection]
        not_knapsack.remove(to_add)
        knapsack.append(to_add)

    return knapsack, not_knapsack

def remove(knapsack, not_knapsack):
    if len(knapsack) < 2:
        return knapsack, not_knapsack
    else:
        selection = random.randint(0, len(knapsack)-1)
        to_remove = knapsack[selection]
        not_knapsack.append(to_remove)
        knapsack.remove(to_remove)

    return knapsack, not_knapsack

def swap(knapsack, not_knapsack):
    if (len(knapsack) < 1) or (len(not_knapsack) < 1):
        return knapsack, not_knapsack
    else:
        selection1 = random.randint(0, len(knapsack)-1)
        selection2 = random.randint(0, len(not_knapsack)-1)
        to_swap1 = knapsack[selection1]
        to_swap2 = not_knapsack[selection2]
        knapsack2 = copy.deepcopy(knapsack)
        not_knapsack2 = copy.deepcopy(not_knapsack)
        knapsack.remove(to_swap1)
        not_knapsack.remove(to_swap2)
        knapsack.append(to_swap2)
        not_knapsack.append(to_swap1)

    return knapsack, not_knapsack


''' ----- SIMULATED ANNEALING ----- '''
def simulated_annealing_knapsack(max_distance, tsp_selection, temperature=simple, bar_utility=bar_utility1, bar_limit=None):

    # select the proper tsp solver
    if tsp_selection == 'greedy':
        tsp_solve = tsp_solver.greedyTour
    elif tsp_selection == 'two-opt':
        tsp_solve = tsp_solver.twoOptTour
    elif tsp_selection == 'random':
        tsp_solve = tsp_solver.randomTour
    elif tsp_selection == 'sa':
        tsp_solve = tsp_solver.simulatedAnnealingTour
    else:
        sys.exit('Not an accepted TSP solver')

    # assign a temperature function
    if temperature == 'simple':
        temp_function = simple
    elif temperature == 'kirkpatrick':
        temp_function = kirkpatrick
    else:
        sys.exit('Not an accepted temperature function solver')

    # check to see if there is a limit to the number of bars in the crawl
    if bar_limit == None:
        bar_limit = float('inf')

    # list to keep track of evolving
    all_distances = []
    all_utilities = []
    all_num = []

    # initialize the knapsack
    knapsack, not_knapsack = initialize_knapsack()

    # calculate initial distance of knapsack
    distance, route = tsp_solve(knapsack)
    utility = knapsack_utility(knapsack, bar_utility)

    all_distances.append(distance)
    all_utilities.append(utility)
    all_num.append(len(route))

    # simulated annealing
    for i in range(1000):

        # decide whether to add, remove, or swap as a function of distance
        p = random.uniform(0, 1)
        if p < (1./3):
            new_knapsack, new_not_knapsack = add(copy.deepcopy(knapsack), copy.deepcopy(not_knapsack))
        elif p < (2./3):
            new_knapsack, new_not_knapsack = remove(copy.deepcopy(knapsack), copy.deepcopy(not_knapsack))
        else:
            new_knapsack, new_not_knapsack = swap(copy.deepcopy(knapsack), copy.deepcopy(not_knapsack))

        # calculate distance and utility of new knapsack
        new_distance, new_route = tsp_solve(new_knapsack)
        new_utility = knapsack_utility(new_knapsack, bar_utility)

        # finalize the changes based on higher utility or temperature function
        if (new_distance <= max_distance) and (len(new_route) < bar_limit + 1):
            if (new_utility > utility) or (random.uniform(0,1) < temp_function(i, utility-new_utility)):
                knapsack = copy.deepcopy(new_knapsack)
                not_knapsack = copy.deepcopy(new_not_knapsack)
                route = copy.deepcopy(new_route)
                utility = new_utility
                distance = new_distance

        all_distances.append(distance)
        all_utilities.append(utility)
        all_num.append(len(route))

    # return the final route and utility
    return (route, all_num, all_distances, all_utilities)
