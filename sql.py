import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE books (book_name TEXT,book_id INTEGER,book_author_name TEXT,book_genre TEXT,book_isbn TEXT,book_copies INTEGER,available TEXT)")
a=input("put : ")
b=id(a)
c=input("put : ")
d=input("put : ")
e=input("put : ")
f=input("put : ")
g=input("put : ")
cursor.execute("INSERT INTO books values(?,?,?,?,?,?,?)".format(a,b,c,d,e,f,g))

connection.close()