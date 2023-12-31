from lib.book_repository import BookRepository
from lib.book import Book

def test_get_all_records(db_connection):
    book_repo = BookRepository(db_connection)
    
    result = book_repo.all()
    
    assert result != None
    assert result == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
        ]
