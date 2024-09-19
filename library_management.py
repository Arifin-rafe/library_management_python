import sqlite3
from sql_data import *
class Book:
    book_dict = []
    def __init__(
        self,
        book_name=None,
        book_author_name=None,
        book_genre=None,
        book_isbn=None,
        book_copies=None,
        available="yes",
    ):
        self.book_id = id(book_name)
        self.book_name = book_name
        self.book_author_name = book_author_name
        self.book_genre = book_genre
        self.book_isbn = book_isbn
        self.book_copies = book_copies
        self.available = available

    def get_book_info(self):
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "book_author_name": self.book_author_name,
            "book_genre": self.book_genre,
            "book_isbn": self.book_isbn,
            "book_copies": self.book_copies,
            "available": self.available,
        }

    def add_book(self):
        sql_add_book()
        # Book.book_dict.append(self.get_book_info())       
        # print()
        # print("Added successfully")
        # print()

    def show_book(self):
        sql_show_books()
        # print("--------Kn0wledge Library BOOK list--------")
        # print()
        # for book in self.book_dict:
        #     print(
        #         "ID : ",
        #         book["book_id"],
        #         "\t",
        #         "Book Name : ",
        #         book["book_name"],
        #         "\t",
        #         "Author : ",
        #         book["book_author_name"],
        #         "\t",
        #         "Genre :",
        #         book["book_genre"],
        #         "\t",
        #         "ISBN :",
        #         book["book_isbn"],
        #         "\t",
        #         "Copy :",
        #         book["book_copies"],
        #         "\t",
        #         "Status : ",
        #         book["available"],
        #     )
        #     print("-----------------------------------------")
        

class User(Book):
    borrow_book_dict = []
    user_librarian_dict = []

    def __init__(
        self, user_name=None, user_password=None, role=None, taken_book_name=None
    ):
        self.user_id = id(user_name)
        self.user_name = user_name
        self.user_password = user_password
        self.role = role
        self.borrow_book_name = taken_book_name
        self.return_book_name = taken_book_name
    
    def get_id(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_password": self.user_password,
            "role": self.role,
        }
    
    def login(self):
        sql_login()
        # if len(User.user_librarian_dict) > 0:
        #     for user in User.user_librarian_dict:                   
        #         if (
        #                 user.get("user_name") == self.user_name
        #                 and user.get("user_password") == self.user_password
        #             ):
        #             print("Welcome to the library--- {}".format(user.get("user_name")))                   
        #         else:
        #             print("Sorry no id found")                   
        # else:           
        #     return print('Create a Id first')
          
    def create_id(self):
        sql_create_user()
        # User.user_librarian_dict.append(self.get_id())
        # print("Id created successfully")
        # print("Please login now")
        # print(User.user_librarian_dict)

    def borrow_book(self):
        sql_borrow_book()
        # for book in Book.book_dict:
        #     if (
        #         self.borrow_book_name == book["book_name"]
        #         and book["available"] == "yes"
        #         and book["book_copies"] > 0
        #     ):
        #         book["book_copies"] = book["book_copies"] - 1
        #         if book["book_copies"] == 0:
        #             book["available"] = "no"
        #         User.borrow_book_dict.append(book)
        #         print("-----Borrowed Books-----")
        #         print()

        #         for book in self.borrow_book_dict:
        #             print(
        #                 "ID : ",
        #                 book["book_id"],
        #                 "\t",
        #                 "Book Name : ",
        #                 book["book_name"],
        #                 "\t",
        #                 "Author : ",
        #                 book["book_author_name"],
        #                 "\t",
        #                 "Genre :",
        #                 book["book_genre"],
        #                 "\t",
        #                 "ISBN :",
        #                 book["book_isbn"],
        #                 "\t",
        #                 "Copy :",
        #                 book["book_copies"],
        #                 "\t",
        #                 "Status : ",
        #                 book["available"],
        #             )
        #     else:
        #         print("Not available")

    def return_book(self):
        sql_return_book()
        # for return_book in User.borrow_book_dict:
        #     if self.return_book_name == return_book["book_name"]: 
        #         for books in Book.book_dict:
        #             if books["book_name"] == self.return_book_name:
        #                 books["book_copies"] = books["book_copies"] + 1
        #                 if books["book_copies"] > 0:
        #                     books["available"] = "yes"
                
        # else:
        #     print("not available")
        #     print(User.borrow_book_dict)

class Librarian(Book):
    def __init__(self, modified_book_name=None):
        self.update_book_name = modified_book_name
            
    def update_book(self):
        sql_update_book()
        # for update_book in Book.book_dict:
        #     if self.update_book_name == update_book["book_name"]:
        #         updated_book_name = input("Enter updated name : ")
        #         updated_author_name = input("Enter updated author name : ")
        #         updated_book_copies = int(input("Enter number of copies : "))
        #         update_book["book_name"] = updated_book_name
        #         update_book["book_author_name"] = updated_author_name
        #         update_book["book_copies"] = updated_book_copies
        #         print("Successfully Book info Updated")
        #     else:
        #         print("Sorry book not found")
    def update_user(self):
        sql_update_user()
        # for update_user in User.user_librarian_dict:
        #     if self.update_book_name == update_user["user_name"]:
        #         updated_user_name = input("Enter updated name : ")
        #         updated_user_password = input("Enter updated password : ")
        #         update_user["user_name"] = updated_user_name
        #         update_user["user_password"] = updated_user_password
        #         print("Successfully user info Updated")
            # else:
            #     print("Sorry book not found")

    def delete_book(self):
        sql_delete_book()
        # for index, book in enumerate(Book.book_dict):
        #     if book["book_name"] == self.update_book_name:
        #         del Book.book_dict[index] 
        #         print("Book deleted successfully")
        
    def delete_user(self):
        sql_delete_user()
        # for index, user in enumerate(User.user_librarian_dict):
        #     if user["user_name"] == self.update_book_name:
        #         del User.user_librarian_dict[index] 
        #         print("User deleted successfully")
        # else:
        #     print("Sorry No user found")   
    def show_users(self):
        sql_show_users()
        # print("--------Kn0wledge Library USERS list--------")
        # print()
        # if len(User.user_librarian_dict) > 0:
        #     for user in User.user_librarian_dict:
        #         print(
        #         "ID : ",
        #         user["user_id"],
        #         "\t",
        #         "User Name : ",
        #         user["user_name"],
        #         "\t",
        #         "Password : ",
        #         user["user_password"],
        #         "\t",
        #         "Role :",
        #         user["role"]
                
        #     )
        #     print("-----------------------------------------")
        # else:
        #     print("User dict is empty")

active_user = True
while active_user:
    print("Login in as : ->")
    print()
    print("1. User")
    print("2. Librarian")

    print()
    number_input = input("Please choose a number (0-2) : ")
    if number_input in "012":
        if number_input == "1":
            print("1. Login as user")
            print("2. Create Account")
            
            user_sign_in_choice = input("Please choose from here : ")
            if user_sign_in_choice == "1":
                user_name_input = input("Please input user name : ")
                user_password_input = input("Please input user password : ")
                my_user_login = User(user_name_input, user_password_input, None, None)            
                my_user_login.login()
                #solve here
                if len(User.user_librarian_dict) > 0:
                    running = True
                else:
                    running = False
                while running: 
                    print("(1) Borrow book")        
                    print("(2) Return book")
                    print('(3) Show all books')                                       
                    print(" 0 to logout")                                                       
                    print()       
                    user_choice = input("Choose an option : ")
                    if user_choice == "1":
                        borrow_book_name_input = input("Enter borrow book name : ")
                        my_borrow_book = User(None, None, None, borrow_book_name_input)
                        my_borrow_book.borrow_book()
                    elif user_choice == "2":
                        return_book_name_input = input("Provide return book name : ")
                        my_return_book = User(return_book_name_input)
                        my_return_book.return_book()
                    elif user_choice =="3":
                        my_show_book = Book()
                        my_show_book.show_book()
                    elif user_choice =="0":
                        print("You logged out as user")
                        running = False
            elif user_sign_in_choice == "2":
                    user_name_input = input("Please input user name : ")
                    user_password_input = input("Please input user password : ")
                    user_confirm_password_input = input("Please input confirm password : ")
                    if user_confirm_password_input == user_confirm_password_input:
                        my_create_account = User(
                        user_name_input, user_password_input, role="user"
                    )
                        my_create_account.create_id()
                    else:
                        print("Sorry password wont match!!!")
        elif number_input == "2":
                print("1. Login as librarian")
                
                user_sign_in_choice = input("Please choose from here : ")
                if user_sign_in_choice == "1":
                    librarian_name_input = input("Please input librarian name : ")
                    librarian_password_input = input("Please input librarian password : ")
                    if librarian_name_input =="rafe" and librarian_password_input == "123":
                        librarian_running = True
                        while librarian_running:
                            print("1. Add a book")
                            print("2. Update a book")
                            print("3. Delete a book")
                            print("4. Update user")
                            print("5. Delete user")
                            print("6. Show library")
                            print("7. Show users")
                            print("0 to logout")
                            user_choice = input("Choose an option : ")
                            if user_choice == "1":
                                book_name_input = input("Enter Book name : ")
                                book_author_input = input("Enter Book author : ")
                                book_genre_input = input("Enter Book genre : ")
                                book_isbn_input = input("Enter Book ISBN : ")
                                book_copies_input = int(input("Enter Book copies : "))
                                my_add_book = Book(
                                book_name_input,
                                book_author_input,
                                book_genre_input,
                                book_isbn_input,
                                book_copies_input,)
                                my_add_book.add_book()
                                print(my_add_book.show_book())
                            elif user_choice == "2":
                                update_book_name_input = input(
                        "Enter the book name you want to update  : "
                    )
                                my_update_book = Librarian(update_book_name_input)
                                my_update_book.update_book()
                            elif user_choice == "3":
                                delete_book_name_input = input(
                            "Enter the book name you want to delete  : "
                            )
                                my_delete_book = Librarian(delete_book_name_input)
                                my_delete_book.delete_book()
                            elif user_choice == "4":
                                update_user_name_input = input(
                            "Enter the user name you want to update  : "
                            )
                                my_update_user_name = Librarian(update_user_name_input)
                                my_update_user_name.update_user()
                            elif user_choice == "5":
                                delete_user_name_input = input(
                            "Enter the user name you want to delete  : "
                            )
                                my_delete_user = Librarian(delete_user_name_input)
                                my_delete_user.delete_user()
                            elif user_choice == "6":
                                my_lib = Book()
                                my_lib.show_book()
                            elif user_choice == "7":
                                my_user_lib = Librarian()
                                my_user_lib.show_users()
                            elif user_choice =="0":
                                print("You logged out as a librarian")
                                librarian_running=False
                
                    else:
                        print("Sorry (name) or (password) won't match!!!--Try again")

        elif number_input == "0":
            active_user = False
        else:
            print("Invalid choice")
            
