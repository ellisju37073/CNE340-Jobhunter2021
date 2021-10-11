from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
from matplotlib import pyplot as plt

hostname="127.0.0.1"
uname="root"
pwd=""
dbname="cdc_1"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

df= pd.read_sql_table('cdc', engine)

print(df)

plt.figure(figsize=(24, 24))
plt.plot(df['collectionDate'], df['InpatBeds_Occ_AnyPat_Est'])
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Beds')
plt.title('ICU over Time', fontsize=16)
plt.show()