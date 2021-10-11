from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas
from sqlalchemy.types import VARCHAR
from datetime import datetime

hostname="128.199.10.43"
uname="pythoneverything"
pwd="Kona1130"
dbname="Finance5"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))


tables = pandas.read_html('https://finance.yahoo.com/quote/NSRPF/history?p=NSRPF')
NOVO=tables[0]
NOVO = NOVO.drop(100)
NOVO = NOVO.drop(0)
NOVO['Date'] =  pandas.to_datetime(NOVO.iloc[:,0].str.replace(', ','-').str.replace(' ','-'),format='%b-%d-%Y')
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

tables_2= pandas.read_html('https://finance.yahoo.com/quote/LOMLF/history?p=LOMLF')
LION=tables_2[0]
LION = LION.drop(100)
LION = LION.drop(0)
LION['Date'] =  pandas.to_datetime(LION.iloc[:,0].str.replace(', ','-').str.replace(' ','-'),format='%b-%d-%Y') #https://stackoverflow.com/questions/53101655/pandas-time-data-does-not-match-format-error-when-the-string-does-match-the
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
NOVO.to_sql('NOVO',con = engine, if_exists = 'append') #https://www.programmersought.com/article/6891234364/ This is the connection to the table https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
LION.to_sql('LION',con = engine, if_exists = 'append')
connection.close() #Close extension to database

connection=engine.connect()
engine.execute('CREATE TABLE NOVO_temp Like NOVO')
engine.execute('INSERT INTO NOVO_temp SELECT DISTINCT (Date), Open, High, Low, Close, Volume FROM NOVO ')
engine.execute('DROP TABLE NOVO')
engine.execute('ALTER TABLE NOVO_temp RENAME TO NOVO')

# Got this from https://stackoverflow.com/questions/8190541/deleting-duplicate-rows-from-sqlite-database
engine.execute('CREATE TABLE LION_temp Like LION')
engine.execute('INSERT INTO LION_temp SELECT DISTINCT (Date), Open, High, Low, Close, Volume FROM LION ')
engine.execute('DROP TABLE LION')
engine.execute('ALTER TABLE LION_temp RENAME TO LION')
connection.close()





