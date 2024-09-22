from sql_data import *
class Book:
    def add_book(self):
        sql_add_book()
        
    def show_book(self):
        sql_show_books()
        
class User(Book):
    
    def login(self):
        sql_login()
          
    def create_id(self):
        sql_create_user()
        
    def borrow_book(self):
        sql_borrow_book()

    def return_book(self):
        sql_return_book()
        
class Librarian(Book):
    def __init__(self, modified_book_name=None):
        self.update_book_name = modified_book_name
            
    def update_book(self):
        sql_update_book()
        
    def update_user(self):
        sql_update_user()
        
    def delete_book(self):
        sql_delete_book()
         
    def delete_user(self):
        sql_delete_user()
          
    def show_users(self):
        sql_show_users()
        
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
                my_user_login = User()            
                my_user_login.login()                
                running = True               
                while running: 
                    print("(1) Borrow book")        
                    print("(2) Return book")
                    print('(3) Show all books')                                       
                    print(" 0 to logout")                                                       
                    print()       
                    user_choice = input("Choose an option : ")
                    if user_choice == "1":
                        my_borrow_book = User()
                        my_borrow_book.borrow_book()
                    elif user_choice == "2":
                        my_return_book = User()
                        my_return_book.return_book()
                    elif user_choice =="3":
                        my_show_book = Book()
                        my_show_book.show_book()
                    elif user_choice =="0":
                        print("You logged out as user")
                        running = False
            elif user_sign_in_choice == "2":
                        my_create_account = User()
                        my_create_account.create_id()
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
                                my_add_book = Book()
                                my_add_book.add_book()
                            elif user_choice == "2":
                                
                                my_update_book = Librarian()
                                my_update_book.update_book()
                            elif user_choice == "3":
                                my_delete_book = Librarian()
                                my_delete_book.delete_book()
                            elif user_choice == "4":
                                my_update_user_name = Librarian()
                                my_update_user_name.update_user()
                            elif user_choice == "5":
                                my_delete_user = Librarian()
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
            
