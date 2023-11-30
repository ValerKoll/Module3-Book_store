from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()
print(connection.DATABASE_NAME)

# Seed with some seed data
connection.seed("seeds/book_store.sql")

book_repo = BookRepository(connection)
books = book_repo.all()

for book in books:
    print(book)




