import pandas
from sqlalchemy import create_engine
import requests
# Use df.to_sql and sqlalchemy https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
# Credentials to database connection
#https://opentechguides.com/how-to/article/pandas/195/pandas-to-mysql.html
hostname="147.182.207.57"
dbname="fantasy_1"
uname="pythoneverything"
pwd="python123"
data = requests.get('https://www.fantasyfootballdatapros.com/api/players/2019/all').json()
df = pandas.json_normalize(data) #Normalize data to be flat
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html#pandas.json_normalize
print(df)
# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))
df.to_sql('fantasy', engine, index=False, if_exists = 'replace')
df.to_excel("fantasy.xlsx")