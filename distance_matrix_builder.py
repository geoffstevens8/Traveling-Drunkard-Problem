import csv
from bs4 import BeautifulSoup
import requests
import time
import json

# import all addresses
addresses = []
with open('biz_list.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        addresses.append(row[1])

# helper function to prepare address for URL
def clean_address(address):
    address = address.replace(',', '')
    address = address.strip()
    address = address.replace(' ', '+')
    return address

# calculate the distance matrix
all_dists = []
all_times = []
for i in range(len(addresses)):
    origin = clean_address(addresses[i])
    dists = []
    times = []
    for j in range(len(addresses)):
        destination = clean_address(addresses[j])

        # create url and send request
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origin + '&destinations=' + destination + '&language=en&units=imperial'
        page = requests.get(url)

        # parse response into json
        soup = BeautifulSoup(page.text, 'html.parser')
        info = soup.text
        d = json.loads(info)

        # select relevant information and add to lsits
        meters = d['rows'][0]['elements'][0]['distance']['value']
        seconds = d['rows'][0]['elements'][0]['duration']['value']
        dists.append(meters)
        times.append(seconds)

    # add to the master list
    all_dists.append(dists)
    all_times.append(times)

distfile = open('distance_matrix.csv', 'wb')
wr = csv.writer(distfile, quoting=csv.QUOTE_ALL)
for dist in all_dists:
    wr.writerow(dist)

timefile = open('time_matrix.csv', 'wb')
wr = csv.writer(timefile, quoting=csv.QUOTE_ALL)
for time in all_times:
    wr.writerow(time)
