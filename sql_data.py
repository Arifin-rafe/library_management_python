import sqlite3
import tabulate
def sql_create_table_books():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    table_query = '''CREATE TABLE IF NOT EXISTS books (book_id integer, book_name text,book_author_name text,book_genre text,book_isbn text,book_copies integer,available text)'''
    my_cursor.execute(table_query)
    print('Book Table created...')
    connection.close()
    
def sql_create_table_user():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    table_query = '''CREATE TABLE IF NOT EXISTS users (user_id integer, user_name text,user_password text,role text)'''
    my_cursor.execute(table_query)
    print('User Table created...')
    connection.close()

def sql_add_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    book_name = input ("Enter book name : ")
    book_id = id(book_name)
    book_author_name = input ("Enter author name : ")
    book_genre = input("Enter book_genre : ")
    book_isbn = input("Enter book_isbn : ")
    book_copies = int(input ("Enter book copies : "))
    available = "yes"
    insert_query = "INSERT INTO books(book_id,book_name,book_author_name,book_genre,book_isbn,book_copies,available) values(?,?,?,?,?,?,?)"
    table_list = my_cursor.execute("""select name from sqlite_master where type='table' and name = 'books';""").fetchall()
    if table_list == []:
        sql_create_table_books()
        my_cursor.execute(insert_query,(book_id,book_name,book_author_name,book_genre,book_isbn,book_copies,available))
    else:
        my_cursor.execute(insert_query,(book_id,book_name,book_author_name,book_genre,book_isbn,book_copies,available))
        print("Data added to DB")
    connection.commit()
    connection.close()
    
def sql_update_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    book_name_update = input ("Enter book name you want to update : ")  
    update_query = "UPDATE books SET book_name=?,book_author_name=?,book_genre=?,book_isbn=?,book_copies=? WHERE book_name=?"
    table_list = my_cursor.execute("""select name from sqlite_master where type='table' and name = 'books';""").fetchall()
    if table_list == []:
        print('No table found')
    else:
        select = "SELECT * FROM books where book_name=?"
        my_cursor.execute(select,(book_name_update,))
        row = my_cursor.fetchone()
        if row == None:
            print("No id found")
        else:
            book_name = input ("Enter book name : ")
            book_author_name = input ("Enter author name : ")
            book_genre = input("Enter book_genre : ")
            book_isbn = input("Enter book_isbn : ")
            book_copies = int(input ("Enter book copies : "))
            my_cursor.execute(update_query,(book_name,book_author_name,book_genre,book_isbn,book_copies))
            print("Data added to DB")
            connection.commit()
            connection.close()
    
def sql_delete_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    book_name = input ("Enter book name you want to delete : ")
    delete_query = "DELETE FROM books WHERE book_name=?"
    table_list = my_cursor.execute("""select name from sqlite_master where type='table' and name = 'books';""").fetchall()
    if table_list == []:
        print('Sorry no table found')
    else:
        my_cursor.execute(delete_query,(book_name,))
        print("Data updated in DB")
    connection.commit()
    connection.close()
    
def sql_show_books():
    print('-------Book list from DB------')
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    select_query = "SELECT * FROM books;"
    table_list = my_cursor.execute("""select name from sqlite_master where type='table' and name = 'books';""").fetchall()
    if table_list == []:
        print("Table not found")
    else:
        my_cursor.execute(select_query)
        rows = my_cursor.fetchall()
        print(tabulate.tabulate(rows,headers=("Id","Name","Author Name","Book Genre","Book ISBN","Copies","Available")))
    connection.commit()
    connection.close()
# while True:
#     print("1. Add")
#     print("2. show book")
#     print("3. Update")
#     print("4. Delete")
#     my_in = input("choose : ")
#     if my_in == "1":
#         sql_add_book()
#     elif my_in == '0':
#         break