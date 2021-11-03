from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
from matplotlib import pyplot as plt

hostname="147.182.207.57"
uname="pythoneverything"
pwd="python123"
dbname="fantasy_1"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

df = pd.read_sql_table('fantasy', engine)

print(df)

plt.figure(figsize=(48, 48))
plt.plot(df['player_name'], df['stats.rushing.rushing_yds'])
plt.xlabel('Name')
plt.xticks(rotation=90)
plt.ylabel('Rushing Yards')
plt.title('2019 Rushing Yard', fontsize=16)
plt.show()
