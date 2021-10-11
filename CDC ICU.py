from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas


hostname="127.0.0.1"
uname="root"
pwd=""
dbname="cdc_1"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

tables = pandas.read_csv(r'https://www.cdc.gov/nhsn/pdfs/covid19/covid19-NatEst.csv')
tables = tables.drop(columns= 'Notes')
tables = tables.drop(0)

connection=engine.connect()
tables.to_sql('cdc', con = engine, if_exists = 'replace')


connection.close() #Close extension to database