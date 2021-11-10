from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
from matplotlib import pyplot as plt

hostname="147.182.207.57"
uname="pythoneverything"
pwd="python123"
dbname="finance"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

df = pd.read_sql_table('novo', engine)

print(df)

plt.figure(figsize=(24, 24))
plt.plot(df['Date'], df['Open'])
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Open')
plt.title('NOVO Over Time', fontsize=16)
plt.show()
