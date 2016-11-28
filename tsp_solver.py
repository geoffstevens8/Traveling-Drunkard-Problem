import csv
from random import shuffle

dist_matrix = []
with open('distance_matrix.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        dist_matrix.append(row)

def getRouteDistance(bars):
  total_distance = 0
  prev_bar = bars[0]
  for i in range(1, len(bars)):
    total_distance += int(dist_matrix[prev_bar][bars[i]])
    prev_bar = bars[i]
  return total_distance



def randomTour(bars):
  """Function returns length of random bar tour and the path of the tour"""
  shuffle(bars)
  total_distance = getRouteDistance(bars)
  return (total_distance, bars)

def greedyTour(bars):
  """
  Function returns length of greedy bar tour and the path of the tour

  Starts by finding the shortest path among all the given bars,
  and then choses the next closest bar until all bars have been visited
  """

  #find the first and second bars greedily
  visited_bars = []
  total_distance = 0
  min_dist = float('inf')
  for i in range(len(bars)):
    for j in range(i + 1, len(bars)):
      if int(dist_matrix[i][j]) < min_dist:
        min_dist = int(dist_matrix[i][j])
        first_bar = i
        second_bar = j
  total_distance += min_dist
  visited_bars.extend([first_bar, second_bar])
  bars = [i for j,i in enumerate(bars) if i not in visited_bars]
  prev_bar = second_bar

  #from the second bar continue to pick the next clostest bar
  while bars:
    min_dist = float('inf') 
    for bar in bars:
      if int(dist_matrix[prev_bar][bar]) < min_dist:
        min_dist = int(dist_matrix[prev_bar][bar])
        next_bar = bar
    total_distance += min_dist
    visited_bars.append(next_bar)
    bars = [i for j,i in enumerate(bars) if i not in visited_bars]
    prev_bar = next_bar
  return (total_distance, visited_bars)

def twoOptSwap(bars, i, k):
  route_begin = bars[:i]
  route_middle = bars[i:k + 1][::-1]
  route_end = bars[k+1:]
  return route_begin + route_middle + route_end


def twoOptTour(bars):
  best_distance = getRouteDistance(bars)
  best_route = bars
  is_swap = True
  while is_swap:
    is_swap = False
    for i in range(len(bars)):
      for k in range(i + 1, len(bars)):
        new_route = twoOptSwap(bars, i, k)
        new_distance = getRouteDistance(new_route)
        if new_distance < best_distance:
          best_distance = new_distance
          best_route = new_route
          is_swap = True
  return (best_distance, best_route)