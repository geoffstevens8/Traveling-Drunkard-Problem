'''

Inputs:
Takes in a maximum distance that will be the constraint.

Outputs:
Final list of bars in order that they should be traveled

'''
import random
import copy

''' KNAPSACK INITIALIZATION '''
def initialize_knapsack():
    # select one bar, return
    # return all bars not in knapsack

''' BAR UTILITY '''
def bar_utility1(bar):
    # some function of cost and stars
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
    return (1./index) + (0.1*utility)



''' ----- SIMULATED ANNEALING ----- '''
def simulated_annealing_knapsack(max_distance, tsp_solver):

    # initialize the knapsack
    knapsack, not_knapsack = initialize_knapsack()

    # calculate initial distance of knapsack
    distance = tsp_solver(knapsack)
    utility = knapsack_utility(knapsack, bar_utility1)

    # simulated annealing
    for i in range(100):

        # decide whether to add, remove, or swap as a function of distance
        p = random.uniform(0, 1)
        if p < (1./3):
            new_knapsack = add(knapsack)
        elif p < (2./3):
            new_knapsack = remove(knapsack)
        else:
            new_knapsack = swap(knapsack)

        # calculate distance and utility of new knapsack
        new_distance = tsp_solver(new_knapsack)
        new_utility = knapsack_utility(new_knapsack)

        # finalize the changes based on higher utility or temperature function
        if new_distance <= max_distance:
            if (new_utility > utility) or (random.random < temperature1(j, new_utility)):
                knapsack = copy.deepcopy(new_knapsack)
                utility = new_utility
                distance = new_distance
