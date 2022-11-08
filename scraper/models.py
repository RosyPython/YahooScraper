from django.db import models
import requests
# Create your models here.


class Stock(models.Model):
    stock_ticker = models.TextField()
    current_price = requests.get(
        f'https://finance.yahoo.com/quote/{{stock_ticker}}?p={{stock_ticker}}&.tsrc=fin-srch')
