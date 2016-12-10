# Traveling-Drunkard-Problem

## Table of Contents

### Python Files
- parser.py: scrapes Yelp for businesses
- distance_matrix_builder.py: builds a matrix of time and distance between all businesses for easy lookup in algorithms
- knapsack.py: implements the simulated annealing to select the best bars for the crawl
- tsp_solver.py: implements the TSP solving algorithms to find the distance of a given knapsack
- config.py: contains scripts to import list of bars and other miscellaneous necessities to run algorithms
- run.py: build a bar crawl, explained below
- run_multiple.py: builds multiple bar crawls for comparison of TSP solvers, explained below

### Data Files
- biz_list.csv: list of businesses with name, address, stars, and price
- distance_matrix.csv: distance between each business, in meters, with the origin on the vertical axis and destination on the horizontal axis. Note: index is equivalent to index in biz_list.csv (e.g. the distance between Business 1 and Business 3 will be Row 1, Column 3)
- time_matrix.csv: travel time between each business, in seconds, with the origin on the x axis and the destination on the y axis. Note: index is equivalent to index in biz_list.csv (e.g. the time between Business 1 and Business 3 will be Row 1, Column 3)

### Building the Ultimate Bar Crawl
Run the file run.py to create a single crawl with the following options:
- --distance DISTANCE: replace DISTANCE with the maximum distance you want for the bar crawl, default is 10,000
- --tsp TSP ALGORITHM: replace TSP ALGORITHM with the TSP solver you wish to use (options: random, greedy, two-opt), default is greedy
- --print-url: add this option if you want a URL to Google Maps with the bar crawl
- --graphs: add this option if you want to print some informational graphs about the crawl
- --temp TEMPERATURE FUNCTION: replace TEMPERATURE FUNCTION with the name of a temperature function for the simulated annealing (options: simple, kirkpatrick)

Example: python run.py --distance 10000 --tsp two-opt --print-url --graphs --temp kirkpatrick

Run the file run_multiple.py to see more data on comparing TSP solvers with the following options:
- --distance DISTANCE: replace DISTANCE with the maximum distance you want for the bar crawl, default is 10,000
- --iterations ITERATIONS: replace ITERATIONS with the number of times you would like to run the crawl generator for each TSP solver, default is 3
- --graphs: add this option if you want to print some informational graphs about the crawl
- --temp TEMPERATURE FUNCTION: replace TEMPERATURE FUNCTION with the name of a temperature function for the simulated annealing (options: simple, kirkpatrick)

Example: python run_multiple.py --distance 10000 --iterations 4 --graphs --temp kirkpatrick

Note: this may take several minutes to run
