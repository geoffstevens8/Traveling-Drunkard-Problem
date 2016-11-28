'''

Inputs:
Takes in a maximum distance that will be the constraint.

Outputs:
Final list of bars in order that they should be traveled

'''

import tsp_solver
import random
import copy
import config


''' KNAPSACK INITIALIZATION '''
def initialize_knapsack():
    # select one bar, return
    # return all bars not in knapsack

    # empty knapsack
    knapsack = []

    # number of bars and list of all indices
    num_bars = len(BAR_LIST)

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
    stars = BAR_LIST[bar][2]
    dollars = len(BAR_LIST[bar][3])

    # utility function of stars and dollars
    utility = stars + (5 - dollars)

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
def temperature1(index, utility):
    return (1./(index+1)) + (1./utility)

''' MUTATE KNAPSACK FUNCTIONS '''
def add(knapsack, not_knapsack):
    selection = random.randint(0, len(not_knapsack)-1)
    to_add = not_knapsack[selection]
    not_knapsack.remove(to_add)
    knapsack.append(to_add)

    return knapsack, not_knapsack

def remove(knapsack, not_knapsack):
    selection = random.randint(0, len(knapsack)-1)
    to_remove = knapsack[selection]
    not_knapsack.append(to_remove)
    knapsack.remove(to_remove)

    return knapsack, not_knapsack

def swap(knapsack, not_knapsack):
    selection1 = random.randint(0, len(knapsack)-1)
    selection2 = random.randint(0, len(not_knapsack)-1)
    to_swap1 = knapsack[selection1]
    to_swap2 = not_knapsack[selection2]
    knapsack.remove(to_swap1)
    not_knapsack.remove(to_swap2)
    knapsack.append(to_swap2)
    not_knapsack.append(to_swap1)

    return knapsack, not_knapsack


''' ----- SIMULATED ANNEALING ----- '''
def simulated_annealing_knapsack(max_distance, tsp_solver, temperature=temperature1, bar_utility=bar_utility1):

    # list to keep track of evolving
    all_distances = []
    all_utilities = []

    # initialize the knapsack
    knapsack, not_knapsack = initialize_knapsack()

    # calculate initial distance of knapsack
    distance, route = tsp_solver(knapsack)
    utility = knapsack_utility(knapsack, bar_utility)

    all_distances.append(distance)
    all_utilities.append(utility)

    # simulated annealing
    for i in range(100):

        # decide whether to add, remove, or swap as a function of distance
        p = random.uniform(0, 1)
        if (p < (1./3)) and (len(not_knapsack) > 0):
            new_knapsack, new_not_knapsack = add(knapsack)
        elif (p < (2./3)) and (len(knapsack) > 0):
            new_knapsack, new_not_knapsack = remove(knapsack)
        else:
            new_knapsack, new_not_knapsack = swap(knapsack)

        # calculate distance and utility of new knapsack
        new_distance, new_route = tsp_solver(new_knapsack)
        new_utility = knapsack_utility(new_knapsack)

        # finalize the changes based on higher utility or temperature function
        if new_distance <= max_distance:
            if (new_utility > utility) or (random.random < temperature(j, new_utility)):
                knapsack = copy.deepcopy(new_knapsack)
                not_knapsack = copy.deepcopy(new_not_knapsack)
                route = copy.deepcopy(new_route)
                utility = new_utility
                distance = new_distance

        all_distances.append(distance)
        all_distances.append(utility)

    # return the final route and utility
    return (route, all_distances, all_utilities)
