import sqlite3
 
#connect the database
conn = sqlite3.connect('projectDatabase.db')
cursor = conn.cursor()

#create the table

cursor.execute("CREATE TABLE IF NOT EXISTS projectDatabase (id Integer Primary key, username Text, password Text)")


#insert data into the table
cursor.execute("INSERT INTO projectDatabase (username, password) VALUES (?,?)", ("panda", "bamboo"))
cursor.execute("INSERT INTO projectDatabase (username, password) VALUES (?,?)", ("dog", "bone"))
cursor.execute("INSERT INTO projectDatabase (username, password) VALUES (?,?)", ("cat", "milk"))
cursor.execute("INSERT INTO projectDatabase (username, password) VALUES (?,?)", ("bird", "seed"))
cursor.execute("INSERT INTO projectDatabase (username, password) VALUES (?,?)", ("squirrel", "acorn"))
cursor.execute("INSERT INTO projectDatabase (username, password) VALUES (?,?)", ("sheep", "grass"))
cursor.execute("INSERT INTO projectDatabase (username, password) VALUES (?,?)", ("horse", "hay"))

#commit changes and close the connection

conn.commit()

#retrieve data from the table
cursor.execute("SELECT * from projectDatabase")

for i in range(7):
    row = cursor.fetchone()
    print(f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}")

conn.close()

#display the retrieved rows


#Close the connection 