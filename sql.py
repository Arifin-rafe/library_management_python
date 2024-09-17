import sqlite3

def create_table_books():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    table_query = '''create table books (book_id integer, book_name text,book_author_name text,book_genre text,book_isbn text,book_copies integer,available text)'''
    my_cursor.execute(table_query)
    print('Book Table created...')
    connection.close()
    
def create_table_user():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    table_query = '''create table users (user_id integer, user_name text,user_password text,role text)'''
    my_cursor.execute(table_query)
    print('User Table created...')
    connection.close()

def add_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    book_name = input ("Enter book name : ")
    book_id = id(book_name)
    book_author_name = input ("Enter author name : ")
    book_genre = input("Enter book_genre : ")
    book_isbn = input("Enter book_isbn : ")
    book_copies = int(input ("Enter book copies : "))
    available = "yes"
    insert_query = "insert into books(book_id,book_name,book_author_name,book_genre,book_isbn,book_copies,available) values(?,?)"
    table_list = my_cursor.execute("""select book_name from """)