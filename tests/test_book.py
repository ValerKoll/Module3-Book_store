from lib.book import Book

"""
Book constructs with an id, name and genre
"""
def test_book():
    book = Book(20, "20 miles under", "Phil")
    assert book.id == 20
    assert book.title == "20 miles under"
    assert book.author_name == "Phil"

"""
We can format books to strings nicely
"""
def test_book_format():
    result = Book(1, "20 miles under", "Phil")
    assert str(result) == "1 - 20 miles under - Phil"

"""
We can compare two identical books
And have them be equal
"""
def test_book_are_equal():
    book1 = Book(20, "20 miles under", "Phil")
    book2 = Book(20, "20 miles under", "Phil")
    assert book1 == book2