import sqlite3

#this is always looking in the current working directory folder
#when built it looks in the executable folder

def connect():
    #relative path based on current working directory
    conn=sqlite3.connect("books.db")
    # conn=sqlite3.connect(".\\bookstore\\books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    # conn=sqlite3.connect(".\\bookstore\\books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    # conn=sqlite3.connect(".\\bookstore\\books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

#this is going to be an "OR" search
# def search(title,author,year,isbn):
#we are passing empty strings in case the user does not supply all 4 arguments
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    # conn=sqlite3.connect(".\\bookstore\\books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    # conn=sqlite3.connect(".\\bookstore\\books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    # conn=sqlite3.connect(".\\bookstore\\books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
#these are examples of how to use the functions above
# insert("The Sun", "John Carter", 1918, 913123122)
# delete(3)
# update(4, "The Moon", "John Smooth", 1917, 9999999)
# print(view())
# print(search(author="John smith"))