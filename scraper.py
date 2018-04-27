# Import libraries
import requests
import csv
from bs4 import BeautifulSoup

infile = open("URLlist.txt", 'r')
urls = infile.readlines()

f = csv.writer(open('output.csv', 'w'))
f.writerow(['Title', 'Discount', 'Previous Price', 'Discounted Price', 'Remaining Time'])

for line in urls:
    page = requests.get(line)
    print(line)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    # Product title
    title = soup.find(class_='product-title')
    title = title.contents[0]
    # Discount
    discount = soup.find(class_='product-discount')
    discount = discount.contents[0]
    # Previous Price
    prevPrice = soup.find(class_='product-price')
    prevPrice = prevPrice.contents[1].contents[0]
    # Discount price
    discPrice = soup.find(class_='product-price')
    discPrice = discPrice.contents[0].contents[0]
    # Coupon Remaining Time
    remainTime = soup.find(class_='minutes')
    remainTime = remainTime.contents[0]




    f.writerow([title,discount,prevPrice,discPrice,remainTime])

    print(remainTime)
    print(title)
    print(discount)
    print(prevPrice)
    print(discPrice)
