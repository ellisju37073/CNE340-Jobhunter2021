from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
import requests


hostname="127.0.0.1"
uname="root"
pwd=""
dbname="finance"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

url = "https://finance.yahoo.com/quote/MSFT/history?p=MSFT"

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"} #https://code-paper.com/typescript/examples-python-requests-firefox-headers#:~:text=python%20requests%20firefox%20headers%20import%20requests%20url%20%3D,like%20Gecko%29%20Chrome%2F39.0.2171.95%20Safari%2F537.36%27%7D%20response%20%3D%20requests.get%28url%2C%20headers%3Dheaders%29
msft= requests.get(url, headers=header)

tables= pd.read_html(msft.text, header = 0)
MSFT=tables[0]
MSFT = MSFT.drop(100)
MSFT = MSFT.drop(0)
MSFT['Date'] =  pd.to_datetime(MSFT.iloc[:, 0].str.replace(', ', '-').str.replace(' ', '-'), format='%b-%d-%Y')
MSFT.set_index('Date', inplace= True)
MSFT= MSFT.sort_values(by="Date")
MSFT["Open"]= MSFT["Open"].astype("str")
MSFT = MSFT[MSFT["Open"].str.contains("Dividend") == False] # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html
MSFT["Open"]= MSFT["Open"].astype("float")
MSFT["High"]= MSFT["High"].astype("float")
MSFT["Low"]= MSFT["Low"].astype("float")
MSFT["Low"]= MSFT["Low"].astype("float")
MSFT["Close*"]= MSFT["Close*"].astype("float")
MSFT["Close*"]= MSFT["Close*"].rename("Close")
MSFT.rename(columns = {"Adj Close**": "Adjusted Close", "Close*": "Close"}, inplace = True)
MSFT = MSFT.drop(columns='Adjusted Close')
MSFT["Volume"] = MSFT["Volume"].replace("-", value="0")
MSFT["Volume"]= MSFT["Volume"].astype("float")



connection=engine.connect() # This is to establish a connection https://docs-sqlalchemy.readthedocs.io/ko/latest/core/connections.html
MSFT.to_sql('msft',con = engine, if_exists = 'append') #https://www.programmersought.com/article/6891234364/ This is the connection to the table https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
connection.close() #Close extension to database

# Got this from https://stackoverflow.com/questions/8190541/deleting-duplicate-rows-from-sqlite-database
engine.execute('CREATE TABLE msft_temp Like msft')
engine.execute('INSERT INTO msft_temp SELECT DISTINCT (Date), Open, High, Low, Close, Volume FROM msft ')
engine.execute('DROP TABLE msft')
engine.execute('ALTER TABLE msft_temp RENAME TO msft')
connection.close()
