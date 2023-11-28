from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

book_repo = BookRepository(connection)
books = book_repo.all()

for book in books:
    print(book)




