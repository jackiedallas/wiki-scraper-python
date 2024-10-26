# Import modules
import requests
from bs4 import BeautifulSoup # type: ignore
import random

# Get request to URL
response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)

# Initialize parser
soup = BeautifulSoup(response.content, 'html.parser')

# Query for the Header and print the String
title = soup.find(id="firstHeading")
print(title.string)