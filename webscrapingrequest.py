import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())