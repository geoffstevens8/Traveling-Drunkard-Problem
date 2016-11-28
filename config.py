import csv

def init():

    global DIST_MATRIX
    DIST_MATRIX = []
    with open('distance_matrix.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            DIST_MATRIX.append(row)

    global TIME_MATRIX
    TIME_MATRIX = []
    with open('time_matrix.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            TIME_MATRIX.append(row)

    global BAR_LIST
    BAR_LIST = []
    with open('biz_list.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            BAR_LIST.append(row)
