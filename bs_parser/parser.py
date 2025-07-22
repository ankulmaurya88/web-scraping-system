# BeautifulSoup parsing logic
from bs4 import BeautifulSoup

def parse_with_bs(html):
    soup = BeautifulSoup(html, 'html.parser')
    return {'title': soup.title.string if soup.title else None}
