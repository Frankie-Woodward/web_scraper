import requests
from bs4 import BeautifulSoup

# Fetch Web Page: Use the requests module to fetch a web page.
url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
web_page = response.text

# Parse HTML: Use BeautifulSoup to parse the HTML.
soup = BeautifulSoup(web_page, 'html.parser')

# Extract Information: Extract the desired information from the parsed HTML.
titles = soup.find_all('title')

for title in titles:
    print(title.get_text())