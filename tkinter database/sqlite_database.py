#5 steps to interact with database
# 1. Connect to database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close connection

#PostgreSQL variables are written like this '%s'
#SQLite variables are written like this '?'

import sqlite3

def create_table():
    #if no db exists will create one
    #will connect if db exists
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    #sql code always goes in as string
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    #use sql to select
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
    

def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    #fast way - prone to SQL Injection
    #cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def delete(_item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (_item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


#create_table()
#update(11,6,"Water Glass")
#delete("Wine Glass")
#insert("Water Glass", 10, 5)
#insert("Coffee Cup", 10, 5)
print(view())