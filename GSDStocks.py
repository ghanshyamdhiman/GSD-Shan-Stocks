import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
import numpy as np

class GSDStock:
  def __init__(self, stock_name):
    self.stock_name = stock_name

  def getStockPrice(self):
    ticker = yf.Ticker(self.stock_name)
    st_info = ticker.info
    stock_price = st_info['regularMarketPrice']
    return stock_price
    
  def getPreviousClosePrice(self):
    ticker = yf.Ticker(self.stock_name)
    st_info = ticker.info
    stock_price = st_info['regularMarketPreviousClose']
    return stock_price
    
  def getStockHistoy(self):
    ticker = yf.Ticker(self.stock_name)
    historic_data = ticker.history(period="1mo", inteval="5d", start="2022-05-01")
    
    return historic_data


  def getStockHistoyCols(self):
    ticker = yf.Ticker(self.stock_name)
    data = ticker.history(period="1mo", inteval="5d", start="2022-05-01")
    historic_data = pd.DataFrame(data, columns=['Open','High'])
    return historic_data

  def getGraph(self):
    ticker = yf.Ticker(self.stock_name)
    data = ticker.history(period="1mo", inteval="5d", start="2022-05-01")
    orig_data = pd.DataFrame(data, columns=['Open','High'])
    orig_data['sl'] = range(1,50)
    orig_data.plot(y="Open", x="sl", kind="line")
    plt.show()
    
    
 