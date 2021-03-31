import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web


# Trens sensitive trading strategy
# Hypothesis: if 7 day mean > 21 day mean == the market is in a positive trend
#             & if 7 day mean < 21 day mean == market is in a negative trend

# ad-hoc: if current price hitting upper bollinger band is associated with an 
# increaded in volume where Volume > Volume1 a recoil is expected. 

#themes: ggplot, classic
style.use('ggplot')

# time inteval
start = dt.datetime(2020,1,1)
end = dt.datetime(2022,1,1)

# S&P 500
#df = web.DataReader('^GSPC','yahoo',start,end)
#df = web.DataReader('VOOG','yahoo',start,end)
#df = web.DataReader('NVDA','yahoo',start,end)
#df = web.DataReader('TSLA','yahoo',start,end)
#df = web.DataReader('AMZN','yahoo',start,end)
#df = web.DataReader('AAPL','yahoo',start,end)
#df = web.DataReader('KLAC','yahoo',start,end)
#df = web.DataReader('AAPL','yahoo',start,end)

#  OMXS  
#df = web.DataReader('^OMX','yahoo',start,end)
#df = web.DataReader('ABB.ST','yahoo',start,end)
#df = web.DataReader('ALFA.ST','yahoo',start,end)
#df = web.DataReader('ALIV-SDB.ST','yahoo',start,end)
#df = web.DataReader('ASSA-B.ST','yahoo',start,end)
#df = web.DataReader('ATCO-A.ST','yahoo',start,end) 
#df = web.DataReader('ATCO-B.ST','yahoo',start,end)
#df = web.DataReader('AZN.ST','yahoo',start,end)
#df = web.DataReader('BOL.ST','yahoo',start,end)
#df = web.DataReader('ELUX-B.ST','yahoo',start,end) 
#df = web.DataReader('ERIC-B.ST','yahoo',start,end)
#df = web.DataReader('ESSITY-B.ST','yahoo',start,end)
#df = web.DataReader('GETI-B.ST','yahoo',start,end) 
#df = web.DataReader('HEXA-B.ST','yahoo',start,end)
#df = web.DataReader('HM-B.ST','yahoo',start,end)
#
df = web.DataReader('INVE-B.ST','yahoo',start,end)
#df = web.DataReader('KINV-B.ST','yahoo',start,end)
#df = web.DataReader('NDA-SE.ST','yahoo',start,end)
#df = web.DataReader('SAND.ST','yahoo',start,end)
#df = web.DataReader('SCA-B.ST','yahoo',start,end)
#df = web.DataReader('SEB-A.ST','yahoo',start,end)
#df = web.DataReader('SECU-B.ST','yahoo',start,end)
#df = web.DataReader('SHB-A.ST','yahoo',start,end)
#df = web.DataReader('SKA-B.ST','yahoo',start,end)
#df = web.DataReader('SKF-B.ST','yahoo',start,end)
#df = web.DataReader('SSAB-A.ST','yahoo',start,end)
#df = web.DataReader('SWED-A.ST','yahoo',start,end)
#df = web.DataReader('SWMA.ST','yahoo',start,end)
#df = web.DataReader('TEL2-B.ST','yahoo',start,end)
#df = web.DataReader('TELIA.ST','yahoo',start,end)
#df = web.DataReader('VOLV-B.ST','yahoo',start,end)
#df = web.DataReader('ABB.ST','yahoo',start,end)


df_ohlc = df['Adj Close'].resample('1D').ohlc()
df_volume = df['Volume'].resample('1D').sum()
print(df_ohlc.head())

df['21ma'] = df['Adj Close'].rolling(window=21).mean()
df['14ema'] = df['Adj Close'].rolling(window=7).mean()
df['14std'] = df['Adj Close'].rolling(window=21).std()

# pseudo-volume upper Bollinger band
df['Volume1'] = df['Volume'].rolling(window=21).mean() + df['Volume'].rolling(window=7).std() 


# Upper and lower Bollinger band's
df['Upper']=df['21ma'] + 2* df['14std']
df['Lower']=df['21ma'] - 2 * df['14std']
print(df.tail(6))


ax1 = plt.subplot2grid((8,1),(0,0), rowspan=6, colspan=1)
ax2 = plt.subplot2grid((8,1),(7,0), rowspan=3, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'],color='red')
ax1.plot(df.index, df['14ema'], color='magenta')
ax1.plot(df.index, df['21ma'], color='blue')
ax1.plot(df.index, df['Upper'],color='black')
ax1.plot(df.index, df['Lower'],color='black')
ax2.plot(df.index, df['Volume'], color='red')
ax2.plot(df.index, df['Volume1'], color = 'black')
#ax2.set_yscale('log')
plt.legend(loc='upper left')
plt.show()
