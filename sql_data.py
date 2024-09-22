import sqlite3
import tabulate
import hashlib
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
    table_query = '''CREATE TABLE IF NOT EXISTS users (user_id INTEGER, user_name TEXT,user_password TEXT,role TEXT)'''
    my_cursor.execute(table_query)
    print('User Table created...')
    connection.close()
    
def sql_create_table_borrow_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    table_query = '''CREATE TABLE IF NOT EXISTS borrow_book (book_id INTEGER, book_name TEXT,book_author_name TEXT,book_genre TEXT,book_isbn TEXT,book_copies INTEGER,available TEXT)'''
    my_cursor.execute(table_query)
    print('Borrow book Table created...')
    connection.close()

def sql_create_user():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    user_name = input ("Enter user name : ")
    user_id = id(user_name)
    user_password = input ("Enter user password : ")
    encoded_password = user_password.encode('utf-8')
    hashed_encode_password = hashlib.sha256(encoded_password)
    hashed_password = hashed_encode_password.hexdigest()
     
    user_confirm_password = input ("Enter user confirm password : ")
    role = "user"
    insert_query = "INSERT INTO users(user_id,user_name,user_password,role) values(?,?,?,?)"
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'users'""").fetchall()
    if user_password == user_confirm_password:
        if table_list == []:
            sql_create_table_user()
            my_cursor.execute(insert_query,(user_id,user_name,hashed_password,role,))
        else:
            my_cursor.execute(insert_query,(user_id,user_name,hashed_password,role,))
            print("Data added to user DB and ID created")
            connection.commit()
            connection.close()
    else:
        print('Check your passwords')

def sql_login():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    user_name = input("Enter user name for DB : ")
    user_password = input("Enter user password for DB: ")
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'users'""").fetchall()
    if table_list == []:
        print('No table found')
    else:
        select_user = "SELECT * FROM users WHERE user_name=? AND user_password=?"
        my_cursor.execute(select_user,(user_name,user_password))
        row = my_cursor.fetchone()
        if row == None:
            print("No user found")
        else:
            print(f"---Welcome to DB Library {row[1]}---")
                     
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
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'books'""").fetchall()
    if table_list == []:
        sql_create_table_books()
        my_cursor.execute(insert_query,(book_id,book_name,book_author_name,book_genre,book_isbn,book_copies,available))
    else:
        my_cursor.execute(insert_query,(book_id,book_name,book_author_name,book_genre,book_isbn,book_copies,available))
        print("Data added to DB")
    connection.commit()
    connection.close()

def sql_borrow_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor() 
    book_name_borrow = input ("Enter book name you want to borrow : ")
    insert_borrow_book = "INSERT INTO borrow_book(book_id,book_name,book_author_name,book_genre,book_isbn,book_copies,available) values(?,?,?,?,?,?,?)"
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'borrow_book'""").fetchall()
    if table_list == []:
        sql_create_table_borrow_book()
    select_query = "SELECT * FROM books WHERE book_name=?"
    my_cursor.execute(select_query,(book_name_borrow,))
    row = my_cursor.fetchone()
    update_query_copy = "UPDATE books SET book_copies=? WHERE book_name=?"
    update_query_available = "UPDATE books SET available=? WHERE book_name=?"
    my_cursor.execute(update_query_copy,(row[5]-1,book_name_borrow),)
    if row[5] == 0:
        my_cursor.execute(update_query_available,('no',book_name_borrow),)
        my_cursor.execute(update_query_copy,(0,book_name_borrow),)       
    print(row)
    if row == None:
        print("Sorry no book found")           
    else:
        print(row)
        if row[6] == 'no':
            print("The book is out of stock")
        else:
            my_cursor.execute(insert_borrow_book,(row[0],row[1],row[2],row[3],row[4],row[5],row[6],))
            print("Book added to (borrow book) table")
            connection.commit()
    connection.close()

def sql_return_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    book_name_return = input ("Enter book name you want to return : ")
    return_query = "SELECT * FROM borrow_book WHERE book_name=?"
    update_query = "UPDATE books SET book_copies=? WHERE book_name=?"
    delete_query = "DELETE FROM borrow_book WHERE book_name=?"
    my_cursor.execute(return_query,(book_name_return,))
    return_book_found = my_cursor.fetchone()
    if return_book_found == None:
        print("Sorry no book found with this name")  
    else:
        my_cursor.execute(update_query,(return_book_found[5]+1,book_name_return,))
        my_cursor.execute(delete_query,(book_name_return,))
        print('Book returned successfully from DB')
        connection.commit()
        connection.close()
    
def sql_update_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    book_name_update = input ("Enter book name you want to update : ")  
    update_query = "UPDATE books SET book_name=?,book_author_name=?,book_genre=?,book_isbn=?,book_copies=? WHERE book_name=?"
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'books'""").fetchall()
    if table_list == []:
        print('No table found')
    else:
        select = "SELECT * FROM books WHERE book_name=?"
        my_cursor.execute(select,(book_name_update,))
        row = my_cursor.fetchone()
        if row == None:
            print("No book found")
        else:
            book_name = input ("Enter book name : ")
            book_author_name = input ("Enter author name : ")
            book_genre = input("Enter book_genre : ")
            book_isbn = input("Enter book_isbn : ")
            book_copies = int(input ("Enter book copies : "))
            my_cursor.execute(update_query,(book_name,book_author_name,book_genre,book_isbn,book_copies,book_name_update))
            print("Data Updated to DB")
            connection.commit()
            connection.close()
            
def sql_update_user():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    user_name_update = input ("Enter user name you want to update : ")  
    update_query = "UPDATE users SET user_name=?,user_password=?,role=? WHERE user_name=?"
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'users'""").fetchall()
    if table_list == []:
        print('No table found')
    else:
        select = "SELECT * FROM users where user_name=?"
        my_cursor.execute(select,(user_name_update,))
        row = my_cursor.fetchone()
        if row == None:
            print("No user found")
        else:
            user_name = input ("Enter user name : ")
            user_password = input ("Enter user password : ")
            role = input ("Enter user or admin: ")
            my_cursor.execute(update_query,(user_name,user_password,role,user_name_update))
            print("User Data Updated to DB")
            connection.commit()
            connection.close()
   
def sql_delete_book():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    book_name_delete = input ("Enter book name you want to delete : ")
    delete_query = "DELETE FROM books WHERE book_name=?"
    select_query = "SELECT * FROM books WHERE book_name=?"
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'books'""").fetchall()
    my_cursor.execute(select_query,(book_name_delete,))
    fetched_delete_data = my_cursor.fetchone()
    if book_name_delete == fetched_delete_data[1]:
        if table_list == []:
            print('Sorry no table found')
        else:
            my_cursor.execute(delete_query,(book_name_delete,))
            print("Book Data deleted in DB")
            connection.commit()
            connection.close()
    else:
        print("Sorry no book found with this name")
        
def sql_delete_user():
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    user_name = input ("Enter user name you want to delete : ")
    delete_query = "DELETE FROM users WHERE user_name=?"
    table_list = my_cursor.execute("""select name FROM sqlite_master WHERE type='table' and name = 'users'""").fetchall()
    if table_list == []:
        print('Sorry no table found')
    else:
        my_cursor.execute(delete_query,(user_name,))
        print("User Data deleted in DB")
        connection.commit()
        connection.close()
    
def sql_show_books():
    print('-------Book list from DB------')
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    select_query = "SELECT * FROM books"
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'books'""").fetchall()
    if table_list == []:
        print("Table not found")
    else:
        my_cursor.execute(select_query)
        rows = my_cursor.fetchall()
        print(tabulate.tabulate(rows,headers=("Id","Name","Author Name","Book Genre","Book ISBN","Copies","Available")))
        connection.commit()
        connection.close()
        
def sql_show_users():
    print('-------Book list from DB------')
    connection = sqlite3.connect("library.db")
    my_cursor = connection.cursor()
    select_query = "SELECT * FROM users"
    table_list = my_cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' and name = 'users'""").fetchall()
    if table_list == []:
        print("Table not found")
    else:
        my_cursor.execute(select_query)
        rows = my_cursor.fetchall()
        print(tabulate.tabulate(rows,headers=("Id","User Name","User password","Role")))
        connection.commit()
        connection.close()

