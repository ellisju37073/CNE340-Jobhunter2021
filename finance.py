import urllib
import urllib.parse
import pyodbc as pyodbc
import pymssql
from sqlalchemy import create_engine

server = "cna330-1.mysql.database.azure.com"
database = "finance"
username = "cnaadmin@cna330-1"
password = "James37073*"

driver = '{ODBC Driver 17 for SQL Server}'

odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
connect_str = "mssql+pymssql://username:password@server/database"


import pandas

tables = pandas.read_html('https://finance.yahoo.com/quote/NSRPF/history?p=NSRPF',index_col = 'Date') #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html and https://www.marsja.se/how-to-use-pandas-read_html-to-scrape-data-from-html-tables/
NOVO=tables[0]
tables_2= pandas.read_html('https://finance.yahoo.com/quote/LOMLF/history?p=LOMLF',index_col = 'Date')
LION=tables_2[0]

engine = create_engine(connect_str) # This is so the script knows where to connect and append the data to https://docs-sqlalchemy.readthedocs.io/ko/latest/core/engines.html
connection=engine.connect() # This is to establish a connection https://docs-sqlalchemy.readthedocs.io/ko/latest/core/connections.html

NOVO.to_sql('NOVO',con = engine, if_exists = 'append') #This is the connection to the table https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
LION.to_sql('LION',con = engine, if_exists = 'append')

engine.execute('DELETE FROM NOVO WHERE rowid NOT IN (SELECT min(rowid) from NOVO Group By Date)') # Got this from https://stackoverflow.com/questions/8190541/deleting-duplicate-rows-from-sqlite-database
engine.execute('DELETE FROM LION WHERE rowid NOT IN (SELECT min(rowid) from LION Group By Date)')

engine.execute('DELETE FROM NOVO WHERE "Date"="*Close price adjusted for splits.**Adjusted close price adjusted for both dividends and splits."') #My own SQL code to remove extra lines
engine.execute('DELETE FROM LION WHERE "Date"="*Close price adjusted for splits.**Adjusted close price adjusted for both dividends and splits."')

connection.close() #Close extension to database