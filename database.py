import sqlite3

connect=sqlite3.connect("email.db")
cursor=connect.cursor()

def create_emails_table():
    cursor.execute(" CREATE TABLE  IF NOT EXISTS emails (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,sender TEXT NOT NULL,receiver TEXT NOT NULL,message TEXT NOT NULL) ")
    connect.commit()

create_emails_table()