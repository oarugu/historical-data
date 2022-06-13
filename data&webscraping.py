import yfinance as yf
import requests as rq
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup

#1
tesla_data = yf.download('TSLA')
head = tesla_data.head()
tail = tesla_data.tail()
print(head, tail)
#2
col = ['revenue in millions']
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue#:~:text=Tesla%20annual%20revenue%20for%202021,a%2014.52%25%20increase%20from%202018.'
rev_gme = rq.get(url)
data = rev_gme.text
soup = BeautifulSoup(data, 'html.parser')
tables = soup.find_all('table', class_="historical_data_table table")
dates_prices = []
for tr in tables[0].find_all('tr'):
    for td in tr.find_all('td'):
        dates_prices.append(td.text)
    
years = dates_prices[0::2]
revenue = dates_prices[1::2]
df = pd.DataFrame(revenue, index= years, columns= col)
print(df)

#3
gme_data = yf.download('GME')
head1 = gme_data.head()
tail1 = gme_data.tail()
print(head1, tail1)


#4
col1 = ['revenue in millions']
url1 = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'
rev_gme1 = rq.get(url)
data1 = rev_gme1.text
soup1 = BeautifulSoup(data1, 'html.parser')
tables1 = soup1.find_all('table', class_="historical_data_table table")
dates_prices1 = []
for tr in tables1[0].find_all('tr'):
    for td in tr.find_all('td'):
        dates_prices1.append(td.text)
    
years1 = dates_prices1[0::2]
revenue1 = dates_prices1[1::2]
df1 = pd.DataFrame(revenue1, index= years1, columns= col1)
print(df1)

#5
tesla_data.reset_index(inplace = True)
gme_data.reset_index(inplace = True)

def make_graph(title, dataframe, axis1, axis2):
    x = [i for i in dataframe[axis1]]
    y = [j for j in dataframe[axis2]]

    plt.plot(x, y)
    plt.xlabel('Date')
    plt.ylabel('Open')
    plt.title(title)
    return plt.show()
#GME chart   
make_graph('GME', gme_data, 'Date', 'Open')
#6
#Tesla chart
make_graph('TSLA', tesla_data, 'Date', 'Open')
