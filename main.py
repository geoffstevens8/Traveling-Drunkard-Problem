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

DIST_MATRIX = []
with open('distance_matrix.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        DIST_MATRIX.append(row)

TIME_MATRIX = []
with open('time_matrix.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        TIME_MATRIX.append(row)

BAR_LIST = []
with open('biz_list.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        BAR_LIST.append(row)


(r, d, u) = simulated_annealing_knapsack(15000, greedyTour)

print(d)
