import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
import plotly.io as pio
import yfinance as yf
def makeList(str):
        if str.__contains__(" ") == False:
            return [str]
        
        else:
            return str.split()

def percentChange(closing_prices, days=1):
    result = [0]
    closing_prices = closing_prices.iloc[::days]

    for x in range(len(closing_prices)-1):
        result.append((closing_prices[x] - closing_prices[x+1])/closing_prices[x])

    return result
def yboxPlots(listEnter, days=30):
    list = makeList(listEnter)
    dfs = []
    boxplotData = pd.DataFrame() 

    for x in list:
        df = yf.Ticker(x).history(period='max')
        #df = data.DataReader(x,'yahoo')
        arr = percentChange(df['Close'], days)
        df = df.iloc[::days]
        df['Percent Change'] = arr 
        dfs.append(df['Percent Change'])

    df = pd.concat(dfs, axis=1)
    df.columns = list

    for x in list:
        df['Tickers'] = x
        temp = df[[x,'Tickers']]
        temp.columns = ['Percent Change', 'Tickers']
        boxplotData = boxplotData.append(temp)

    fig = px.box(boxplotData, x = 'Tickers', y = 'Percent Change')
    fig.update_layout(template='plotly_dark')
    pio.write_html(fig, file='static/ticker/boxPlot.html', auto_open=True)

yboxPlots('GOOG AAPL')

