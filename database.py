import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
Create table if not exists students(
    id integer primary key autoincrement,
    name text not null,
    roll_no text not null ,
    branch text not null,
    semester text not null
)
""")

cursor.execute("""
create table if not exists users(
    id integer primary key autoincrement,
    username text unique not null,
    password text not null)
""")

conn.commit()

print("Table created successfully")

conn.close()