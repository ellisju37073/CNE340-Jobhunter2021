from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
from matplotlib import pyplot as plt

hostname="127.0.0.1"
uname="root"
pwd=""
dbname="finance"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

df = pd.read_sql_table('msft', engine)

print(df)

plt.figure(figsize=(24, 24))
plt.plot(df['Date'], df['Open'])
plt.xlabel('Date', fontsize = 36)
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=24)
plt.ylabel('Open', fontsize = 36)
plt.tick_params(axis='y', labelsize=24)
plt.title('MSFT Over Time', fontsize=36)
plt.savefig('image.png')
plt.show()
