"""
This project is a copy of the bookstore application.
The difference is that this is an object oriented programming approach

All of the connection and cursor commands were removed from each function/method
All of the closing statements have been reomved from each function/method
"""

import sqlite3

class Database:

    #when you call a method of a class, the class is sending the object method of the class as well
    #so pass the "self" parameter to the method arguments
    def __init__(self, db):
        #relative path based on current working directory
        # conn=sqlite3.connect("books.db")
        self.conn=sqlite3.connect(db)
        # conn=sqlite3.connect(".\\bookstore\\books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        #going to leave it open...
        #conn.close()

    def insert(self, title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    #this is going to be an "OR" search
    # def search(title,author,year,isbn):
    #we are passing empty strings in case the user does not supply all 4 arguments
    def search(self, title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? or author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()

    #executed when script is exited.
    #always close the database connection
    def __del__(self):
        self.conn.close()


#these are examples of how to use the functions above
# insert("The Sun", "John Carter", 1918, 913123122)
# delete(3)
# update(4, "The Moon", "John Smooth", 1917, 9999999)
# print(view())
# print(search(author="John smith"))