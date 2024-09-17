import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()


connection.close()