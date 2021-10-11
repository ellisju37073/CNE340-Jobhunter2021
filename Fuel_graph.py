from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
from matplotlib import pyplot as plt

hostname="157.245.167.255"
uname="pythoneverything"
pwd="Kona1130"
dbname="Finance5"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

df = pd.read_sql_table('Fuel', engine)

print(df)

plt.figure(figsize=(24, 24))
plt.plot(df['Date'], df['Diesel_Price'])
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Open')
plt.title('Diesel Over Time', fontsize=16)
plt.show()
