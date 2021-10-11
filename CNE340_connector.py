import mysql.connector
conn = mysql.connector.connect(user='root', password='',
                                   host='127.0.0.1', database='cne340')
cursor= conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS hosts(id INTEGER, hostname TEXT, "
               "url TEXT, ip TEXT, local_remote TEXT, description TEXT);")
cursor.execute("INSERT INTO hosts (id, hostname, url, ip, local_remote, description"
               ") VALUES (0, 'loopback', 'localhost', '127.0.0.1', 'local', 'Local DB');")
conn.commit()
cursor.execute("SELECT hostname, url, ip, description FROM hosts")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()