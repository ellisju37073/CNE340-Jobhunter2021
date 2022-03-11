import pandas
from sqlalchemy import create_engine

hostname="161.35.225.132"
uname="justin"
pwd="kona"
dbname="fuel"


engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))


tables = pandas.read_excel ('https://www.eia.gov/dnav/pet/hist_xls/EMD_EPD2DXL0_PTE_R5XCA_DPGw.xls', sheet_name='Data 1',
                                    header = 2, index_col='Date')
tables.rename(columns = {'Weekly West Coast (PADD 5) Except California No 2 Diesel Ultra Low Sulfur (0-15 ppm) Retail Prices  (Dollars per Gallon)'
                         :'Diesel_Price'}, inplace=True)

connection=engine.connect()
tables.to_sql('fuel', con = engine, if_exists = 'append')

engine.execute('CREATE TABLE fuel_temp Like fuel')
engine.execute('INSERT INTO fuel_temp SELECT DISTINCT (Date), Diesel_Price FROM fuel ')
engine.execute('DROP TABLE fuel')
engine.execute('ALTER TABLE fuel_temp RENAME TO fuel')

connection.close() #Close extension to database