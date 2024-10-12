from bs4 import BeautifulSoup
import requests

url = 'https://www.geeksforgeeks.org/courses/dsa-self-paced'
# We are going to send a request
result = requests.get(url)
# print(result.text)

# Parsing the document / content using the beautiful soup.
doc = BeautifulSoup(result.text , 'html.parser')
print(doc.prettify())

# Find the prices with the help of dollars sign.
prices = doc.find_all('p')
# print(prices.text)
parent = prices[0].parent;
print('\n')
print(parent)