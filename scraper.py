from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://aviationweather.gov/metar/data?ids=WSSL&format=decoded&date=&hours=0&taf=on"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()

request_page.close()


html_soup = BeautifulSoup(page_html, 'html parser')

metartaf = html_soup.find_all('table')


filename = 'products.csv'
f = open(filename, 'w')
