import sqlite3
DB='dentasure.db'
def conn():
    c=sqlite3.connect(DB,check_same_thread=False);c.row_factory=sqlite3.Row;return c
def init_db():
    db=conn();cur=db.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,email TEXT UNIQUE,password TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS claims(id INTEGER PRIMARY KEY,user_email TEXT,amount REAL,status TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS assessments(id INTEGER PRIMARY KEY,user_email TEXT,score INTEGER)')
    db.commit();db.close()
