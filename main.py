'''
Notes:
goal -> bar crawl in Boston
    - best bar crawl
    - most stars, cheapest cost, shortest distance
    - consolidate stars / price -> number ('utility')

Start:
1. Pick max distance for algo

1. Knapsack
    - simulated annealing
    - changes: remove, swap, add

2. TSP
    - takes in list of bars
    - finds the shortest path between them all

Ongoing Questions
1. Do we want a starting place?
2. Where to import the CSVs and convert to ints


Interesting Things to Explore
1. bar utility functions
2. different TSP solvers
3. weighting of swap, remove, add functions in simulated annealing

'''
import csv
import knapsack
from tsp_solver import greedyTour
import config

config.init()

print(BAR_LIST)

(r, d, u) = knapsack.simulated_annealing_knapsack(15000, greedyTour)

print(d)
