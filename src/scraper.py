# Import modules
import requests
from bs4 import BeautifulSoup # type: ignore
import random

# Get request to URL
response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)

# Function for scraping
def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    # Initialize parser
    soup = BeautifulSoup(response.content, 'html.parser')

    # Query for the Header and print the String
    title = soup.find(id="firstHeading")
    print(title.text)

    # Get all links on page
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    # Loop through all the links on the page and only get the Wiki Articles
    for link in allLinks:
        if link['href'].find("/wiki/") == -1:
            continue

        # Get a random wiki link
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

# Call function
scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
