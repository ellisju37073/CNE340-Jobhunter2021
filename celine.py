# Celine Watcharaapakorn-Smith
# Abibatou Diop
# Bashar Abduljaleel
# 03.05.23
# Group Project on The COVID Tracking https://data.cdc.gov/api/views/9mfq-cb36/rows.csv

import mysql.connector
import csv
import numpy as np
import pandas as pd
import datetime
from sqlalchemy import create_engine
from sqlalchemy import text
import matplotlib.pyplot as plt

# # Reviewing the data # #
#https://api.covidtracking.com/v1/us/daily.csv
#https://data.cdc.gov/api/views/9mfq-cb36/rows.csv
online_data = r'https://api.covidtracking.com/v1/us/daily.csv'
tables = pd.read_csv(online_data)
print(tables.head(10))  # getting first 10 entries of dataframe
print(tables.tail(10))  # getting last 10 entries of dataframe
# how big is this data
tables.shape
print("This data has {} rows and {} columns.".format(tables.shape[0], tables.shape[1]))
# review columns
print(tables.columns)
# review variable types and names
print(tables.dtypes)

# install cryptography
hostname="127.0.0.1"
username="root"
passwd=""
db_name="FluffyTrack"

# install pymysql and sqlalchemy
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=db_name, user=username, pw=passwd))
# review and download data
tables = pd.read_csv('https://api.covidtracking.com/v1/us/daily.csv')
#tables = pd.read_csv('https://api.covidtracking.com/v1/us/daily.csv')
tables.rename(columns = {'submission_date':'date'}, inplace=True) #rename for better understanding on data

# connect to db
connection=engine.connect()
# create table
tables.to_sql('covid', con = engine, if_exists = 'append')
# create second table for DISC details
connection.execute(text('CREATE TABLE covid_2 Like covid'))
connection.execute(text('INSERT INTO covid_2 SELECT DISTINCT * FROM covid'))
# drop covid table and rename covid_2 to covid
connection.execute(text('DROP TABLE covid'))
connection.execute(text('ALTER TABLE covid_2 RENAME TO covid'))

#df = pd.read_sql_table('covid', connection)
#https://eazybi.com/blog/data-visualization-and-chart-types
df = pd.read_csv('https://api.covidtracking.com/v1/us/daily.csv')

# type of hospitalized patients
fig, ax = plt.subplots()
patients = ['positive', 'negative', 'pending', 'hospitalized']
counts = [28756489, 74582825, 3548787, 776361]
bar_labels = ['pink', 'green', 'orange', 'purple']
bar_colors = ['tab:pink', 'tab:green', 'tab:orange', 'tab:purple']

ax.bar(patients, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('patients supply')
ax.set_title('Hospitalized Patients')
ax.legend(title='Patients')

plt.show()

# types of hospitalization
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
fig, ax = plt.subplots()
labels = 'Regular Hospital Care', 'Intensive Care', 'On Ventilation'
sizes = [df['hospitalizedCumulative'].max(), df['inIcuCumulative'].max(), df['onVentilatorCumulative'].max()]
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.show()

# hospitalized vs deaths
fig, ax = plt.subplots()
ax.plot(df['date'], df['death'], label='Deaths')
ax.plot(df['date'], df['hospitalized'], label='Hospitalizations')
ax.set_xlabel('Date')
ax.set_ylabel('Number of People')
ax.set_title('Deaths and Hospitalizations Due to COVID-19 in the United States')
ax.legend()

plt.show()

connection.close