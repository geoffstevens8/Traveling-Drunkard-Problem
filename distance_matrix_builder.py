import csv
from bs4 import BeautifulSoup
import requests
import time
import json

# import all addresses
addresses = []
with open('biz_list_2.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        addresses.append(row[1])

# open up the csvs to write to
distfile = open('distance_matrix_2.csv', 'wb')
dr = csv.writer(distfile, quoting=csv.QUOTE_ALL)

timefile = open('time_matrix_2.csv', 'wb')
wr = csv.writer(timefile, quoting=csv.QUOTE_ALL)

# helper function to prepare address for URL
def clean_address(address):
    address = address.replace(',', '')
    address = address.strip()
    address = address.replace(' ', '+')
    return address

# calculate the distance matrix
for i in range(len(addresses)):
    origin = clean_address(addresses[i])
    dists = []
    times = []
    print(i)
    for j in range(len(addresses)):
        destination = clean_address(addresses[j])

        # create url and send request
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origin + '&destinations=' + destination + '&language=en&units=imperial&mode=walking'
        page = requests.get(url)

        # parse response into json
        soup = BeautifulSoup(page.text, 'html.parser')
        info = soup.text
        d = json.loads(info)

        # select relevant information and add to lists
        try:
            meters = d['rows'][0]['elements'][0]['distance']['value']
        except IndexError:
            meters = 0

        try:
            seconds = d['rows'][0]['elements'][0]['duration']['value']
        except IndexError:
            seconds = 0

        dists.append(meters)
        times.append(seconds)

    # write to the csvs as we go
    dr.writerow(dists)
    wr.writerow(times)
