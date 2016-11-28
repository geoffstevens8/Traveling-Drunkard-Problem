import csv
from random import shuffle

dist_matrix = []
with open('distance_matrix.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        dist_matrix.append(row)

def randomTour(bars):
  """Function returns length of random bar tour and the path of the tour"""
  shuffle(bars)
  total_distance = 0
  prev_bar = bars.pop(0)
  for bar in bars:
    total_distance += int(dist_matrix[prev_bar][bar])
    prev_bar = bar
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

result = randomTour(range(20))
print result