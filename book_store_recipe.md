# == BOOK STORE ==
## Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table


```
Table: books

Columns:
title | author_name

Values:
('Nineteen Eighty-Four', 'George Orwell')
('Mrs Dalloway', 'Virginia Woolf')
('Emma', 'Jane Austen')
('Dracula', 'Bram Stoker')
('The Age of Innocence', 'Edith Wharton')
```

## 2. Create Test SQL seeds

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 book_store < seeds_book_store.sql
```

## 3. Define the class names

```python
# Model Class
class book

# Repository class
class book_repository
```

## 4. Implement the Model class

```python

# Model class
class Book:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""

```


## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# Repository class
class book_repository():
    def __init__(self, connection):
        self._connection = connection
    
    # Selecting all records
    # No arguments
    def all():
        # execute "SELECT * FROM books" query > connection
        # create instance based on each rows
        # append result to a book list
        # Returns an array of Student objects.
```

## 6. Write Test Examples

```python

### book
"""
Book constructs with an id, name and genre
"""
test_book

"""
We can format books to strings nicely
"""
test_book_format

"""
We can compare two identical books
And have them be equal
"""
test_book_are_equal


### book repo
"""
When we call BookRepository#all
We get a list of Books objects reflecting the seed data.
"""
test_get_all_record
```




## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```
output
id - title - author
id - title - author
id - title - author
id - title - author
```