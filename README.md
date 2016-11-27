# Traveling-Drunkard-Problem

## Table of Contents

### Python Files
- parser.py: scrapes Yelp for businesses
- distance_matrix_builder.py: builds a matrix of time and distance between all businesses for easy lookup in algorithms

### Data Files
- biz_list.csv: list of businesses with name, address, stars, and price
- distance_matrix.csv: distance between each business, in meters, with the origin on the vertical axis and destination on the horizontal axis. Note: index is equivalent to index in biz_list.csv (e.g. the distance between Business 1 and Business 3 will be Row 1, Column 3)
- time_matrix.csv: travel time between each business, in seconds, with the origin on the x axis and the destination on the y axis. Note: index is equivalent to index in biz_list.csv (e.g. the time between Business 1 and Business 3 will be Row 1, Column 3)
