import csv, sqlite3

sqlite_file = "dataimporter.db"
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS hosts(ID INTEGER PRIMARY KEY AUTOINCREMENT,'
               'Lab_Name TEXT, Phone TEXT, Hours TEXT, Tech_Support_Assisted TEXT, Organization TEXT, Location TEXT, Web_address TEXT)')

with open(r'C:\Users\ellis\Downloads\Public_Computer_Access_Locations_nocommas (3).csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Lab_name'], i['Phone'], i['Hours'], i['Tech_Support_Assisted'], i['Organization'], i['Location'], i['Web_address']) for i in dr]

cursor.executemany("INSERT INTO hosts (Lab_Name, Phone, Hours, Tech_Support_Assisted, Organization, Location, Web_address)"
                   "VALUES (?, ?, ?, ?, ?, ?, ?)", to_db)

cursor.execute("SELECT Lab_Name, Phone, Location from hosts WHERE Tech_Support_Assisted = 'Yes'")

rows = cursor.fetchall()
print('Support Assisted Locations:')
for row in rows:
    print(row)

connection.commit()
connection.close()
