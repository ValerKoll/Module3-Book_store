from lib.book import Book

class BookRepository():
    def __init__(self, connection):
        self._connection = connection
    
    # Selecting all records
    # No arguments
    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            book = Book(row['id'], row['title'], row['author_name'])
            books.append(book)
        return books
        # execute "SELECT * FROM books" query > connection
        # create instance based on each rows
        # append result to a book list
        # Returns an array of Student objects.