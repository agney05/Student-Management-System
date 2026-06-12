import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("select * from users")

print(cursor.fetchall())

conn.close()