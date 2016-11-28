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
4. temperature functions
5. max distance allowed


'''
import csv
import knapsack
import tsp_solver
import config
import matplotlib.pyplot as plt
import numpy as np

(r, d, u) = knapsack.simulated_annealing_knapsack(50000, tsp_solver.greedyTour)

'''
plot some stuff with 2 axes with different scales
'''

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
plt.show()

print(len(r))
