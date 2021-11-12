import yfinance as yf
import datetime




#d = yf.Ticker('GOOG').history(start = datetime.datetime(2020,1,1), end = datetime.datetime(2020,2,1))
msft = yf.Ticker("MSFT")
hist = msft.history(period="max")