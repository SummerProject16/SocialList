import requests
from bs4 import BeautifulSoup
def trade(max_pages):
    page = 1
    while page < max_pages:
        url = "https://buckysroom.org/trade/search.php?page=" +str(page)
        source_code = requests.get(url)
        plain_text = source_code.text()