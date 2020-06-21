import numpy as np
import requests
from bs4 import BeautifulSoup

userin = input("Enter the Product you want to search: ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def flip(userin):
    text = userin.replace(" ", "%20")
    flip_url = "https://www.flipkart.com/search?q=" + text + "&otracker=search&otracker1=search&marketplace=FLIPKART"
    flip_requests = requests.get(flip_url)
    flip_content = flip_requests.content
    flip_soup = BeautifulSoup(flip_content, "html.parser")
    item, price = [], []
    for element in flip_soup.find_all("div", {"class": "_3wU53n"}):
        item.append("Flipkart, " + element.text)
    for element1 in flip_soup.find_all("div", {"class": "_1vC4OE _2rQ-NK"}):
        price.append(element1.text.strip('₹').replace(",", " ").replace(" ", ""))
    dictionary = list(zip(item, price))

    def takesecond(elem):
        return elem[1]

    srt = sorted(dictionary, key=takesecond)
    srt = np.array(srt)
    return srt

def amazon(userin):
    text = userin.replace(" ", "+")
    amazon_url = "https://www.amazon.in/s?k=" +text+ "&ref=nb_sb_noss_2"
    print(amazon_url)
    amz_requests = requests.get(amazon_url, headers=headers)
    amz_content = amz_requests.content
    amz_soup = BeautifulSoup(amz_content, "html.parser")
    item, price = [], []
    for element in amz_soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"}):
        item.append("Amazon, " + element.text)
    for element1 in amz_soup.find_all("span", {"class": "a-price-whole"}):
        price.append(element1.text.strip('₹').replace(",", " ").replace(" ", ""))
    dictionary = list(zip(item, price))

    def takesecond(elem):
        return elem[1]

    srt = sorted(dictionary, key=takesecond)
    srt1 = np.array(srt)
    return srt1

print(amazon(userin))