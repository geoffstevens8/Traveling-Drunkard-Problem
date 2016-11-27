# Traveling-Drunkard-Problem

## Table of Contents

### Python Files
- parser.py: scrapes Yelp for businesses
- distance_matrix_builder.py: builds a matrix of time and distance between all businesses for easy lookup in algorithms

### Data Files
- biz_list.csv: list of businesses with name, address, stars, and price
- distance_matrix.csv: distance between each business, in meters, with the origin on the x axis and destination on the y axis. Note: index is equivalent to index in biz_list.csv (i.e. the first business in the list of businesses will be the first entry on the x and y axis of the distance matrix)
- time_matrix.csv: travel time between each business, in seconds, with the origin on the x axis and the destination on the y axis. Note: index is equivalent to index in biz_list.csv (i.e. the first business in the list of businesses will be the first entry on the x and y axis of the distance matrix)
