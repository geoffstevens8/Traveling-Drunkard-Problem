from bs4 import BeautifulSoup
import requests
import string
import csv
import time

# master list of all businesses
allbiz = []

# iterate over Yelp pages
for pagenum in range(0, 41, 10):
    time.sleep(15)
    page = requests.get("https://www.yelp.com/search?find_desc=Bars&find_loc=Boston,+MA&start=" + str(pagenum))
    soup = BeautifulSoup(page.text, 'html.parser')
    businesses = soup.find_all("li", attrs={"class": "regular-search-result"})

    # grab all businesses from a page and iterate over each
    for business in businesses:
        # name of the business
        name = business.find("a", attrs={"class": "biz-name"}).text
        name = name.encode("utf8")
        name = name.replace("\xe2\x80\x99", "'")

        # address of the business
        address = str(business.find("address"))
        address = address.replace('<address>', '')
        address = address.replace('</address>', '')
        address = address.replace('<br>', ' ')
        address = address.replace('</br>', '')
        address = address.replace('/n', '')
        address = address.replace('/n', '')
        address = address.strip()

        # stars per business
        stars = str(business.find("div", attrs={"class": "i-stars"})["title"])
        stars = stars.replace('star rating', '')
        stars = stars.strip()

        # price range of the business
        price = str(business.find("span", attrs={"class": "price-range"}).text)
        price = price.strip()

        # final list
        allbiz.append([name, address, stars, price])

# display the final list of businesses
print(allbiz)

# write all of the businesses to a csv file
myfile = open('biz_list_2.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
for biz in allbiz:
    wr.writerow(biz)
