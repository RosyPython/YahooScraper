from django import template
import requests
from bs4 import BeautifulSoup
register = template.Library()


@register.simple_tag(name='get_price')
def get_price(stock_ticker):
    response = requests.get(
        f'https://finance.yahoo.com/quote/{stock_ticker}?p={stock_ticker}&.tsrc=fin-srch')
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.select_one("fin-streamer.Fw\(b\):nth-child(1)").get_text()
