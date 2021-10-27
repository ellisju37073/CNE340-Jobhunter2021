from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
import requests

hostname="147.182.207.57"
uname="pythoneverything"
pwd="python123"
dbname="finance"


engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))
url = "https://finance.yahoo.com/quote/NSRPF/history?p=NSRPF"

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
novo= requests.get(url, headers=header)

tables= pd.read_html(novo.text, header = 0)
NOVO=tables[0]
NOVO = NOVO.drop(100)
NOVO = NOVO.drop(0)
NOVO['Date'] =  pd.to_datetime(NOVO.iloc[:,0].str.replace(', ','-').str.replace(' ','-'),format='%b-%d-%Y')
NOVO.set_index('Date', inplace= True)
NOVO= NOVO.sort_values(by= "Date")
NOVO["Open"]= NOVO["Open"].astype("float")
NOVO["High"]= NOVO["High"].astype("float")
NOVO["Low"]= NOVO["Low"].astype("float")
NOVO["Low"]= NOVO["Low"].astype("float")
NOVO["Close*"]= NOVO["Close*"].astype("float")
NOVO["Close*"]= NOVO["Close*"].rename("Close")
NOVO["Adj Close**"]= NOVO["Adj Close**"].astype("float")
NOVO.rename(columns = {"Adj Close**":"Adjusted Close", "Close*":"Close"}, inplace = True)
NOVO = NOVO.drop(columns= 'Adjusted Close')
NOVO["Volume"] = NOVO["Volume"].replace("-",value="0")
NOVO["Volume"]= NOVO["Volume"].astype("float")


header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
url2 = "https://finance.yahoo.com/quote/LOMLF/history?p=LOMLF"
lion= requests.get(url2, headers=header)
tables_2= pd.read_html(lion.text, header = 0)
LION=tables_2[0]
LION = LION.drop(100)
LION = LION.drop(0)
LION['Date'] =  pd.to_datetime(LION.iloc[:,0].str.replace(', ','-').str.replace(' ','-'),format='%b-%d-%Y') #https://stackoverflow.com/questions/53101655/pandas-time-data-does-not-match-format-error-when-the-string-does-match-the
LION.set_index('Date', inplace= True)
LION= LION.sort_values(by= "Date")
LION["Open"]= LION["Open"].astype("float")
LION["High"]= LION["High"].astype("float")
LION["Low"]= LION["Low"].astype("float")
LION["Close*"]= LION["Close*"].astype("float")
LION["Adj Close**"]= LION["Adj Close**"].astype("float")
LION.rename(columns = {"Adj Close**":"Adjusted Close", "Close*":"Close"}, inplace = True)
LION = LION.drop(columns= 'Adjusted Close')
LION["Volume"] = LION["Volume"].replace("-",value="0")
LION["Volume"]= LION["Volume"].astype("float")

connection=engine.connect() # This is to establish a connection https://docs-sqlalchemy.readthedocs.io/ko/latest/core/connections.html
NOVO.to_sql('novo',con = engine, if_exists = 'append') #https://www.programmersought.com/article/6891234364/ This is the connection to the table https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
LION.to_sql('lion',con = engine, if_exists = 'append')
connection.close() #Close extension to database

connection=engine.connect()
engine.execute('CREATE TABLE novo_temp Like novo')
engine.execute('INSERT INTO novo_temp SELECT DISTINCT (Date), Open, High, Low, Close, Volume FROM novo ')
engine.execute('DROP TABLE novo')
engine.execute('ALTER TABLE novo_temp RENAME TO novo')

# Got this from https://stackoverflow.com/questions/8190541/deleting-duplicate-rows-from-sqlite-database
engine.execute('CREATE TABLE lion_temp Like lion')
engine.execute('INSERT INTO lion_temp SELECT DISTINCT (Date), Open, High, Low, Close, Volume FROM lion ')
engine.execute('DROP TABLE lion')
engine.execute('ALTER TABLE lion_temp RENAME TO lion')
connection.close()





