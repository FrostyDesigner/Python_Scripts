#5 steps to interact with database
# 1. Connect to database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close connection

#PostgreSQL variables are written like this '%s'
#SQLite variables are written like this '?'

import psycopg2

def create_table():
    #if no db exists will create one
    #will connect if db exists
    #no commas needed in connection string - entire object is passed as a string
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Synergy1' host='localhost' port='5432'")
    cur=conn.cursor()
    #sql code always goes in as string
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Synergy1' host='localhost' port='5432'")
    cur=conn.cursor()
    #use sql to select
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
    

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Synergy1' host='localhost' port='5432'")
    cur=conn.cursor()
    #note that the PsotgreSQL way is different than the sqlite way
    #fast way - prone to SQL Injection
    # cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    #proper way with parameters
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def delete(_item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Synergy1' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (_item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Synergy1' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

#create_table()
#update(50,25,"Orange")
#delete("Banana")
#insert("Banana", 13, 8)
print(view())