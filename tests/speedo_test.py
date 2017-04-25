#import pytest for testing framework
import pytest
import inspect

#import the code we're testing
from speedo import *

#smoke test
def test_smoke():
    assert True

#test to calculate pages read per minute
def test_it_can_calculate_ppm():
    pages_read = 100 # number of pages
    time_spent = 180 # minutes spent reading
    assert calc_ppm(pages_read, time_spent) == 100/180 #check
    assert calc_ppm(200, 50) == 4 #double check without variables

# test to check if the class "Book" exists
def test_book_class_exists():
    assert inspect.isclass(Book)

# test to see if you can create an instance within the Book class
def test_it_can_create_a_book_instance():
    harry_potter = Book()
    assert isinstance(harry_potter, Book)

# test to give a book a platform descriptor
def test_a_book_has_a_platform():
    harry_potter = Book("print")
    twilight = Book("ebook")
    assert hasattr(harry_potter, "platform") # Check that the property exists
    assert harry_potter.platform == "print" # and that is has the expected value
    assert twilight.platform == "ebook"
    # and that it can be set to something else

# test to check if the book's properties can be set in order
def test_it_can_set_properties_by_order():
    harry_potter = Book("e-book", "Harry Potter", 254, 360)
    assert harry_potter.platform == "e-book"
    assert harry_potter.title == "Harry Potter"
    assert harry_potter.pages == 254
    assert harry_potter.minutes == 360

#test to see if you can choose the order you want to display book properties
def test_it_can_set_properties_by_name():
    harry_potter = Book(title="Harry Potter", pform="e-book")
    assert harry_potter.platform == "e-book"
    assert harry_potter.title == "Harry Potter"
    assert harry_potter.pages == 100
    assert harry_potter.minutes == 100

#test to check ppm reporting
def test_a_book_and_report_ppm():
    harry_potter = Book(title="Harry Potter")
    assert harry_potter.ppm() == 1

#test to create an array of books
def test_length_array_of_books():
    books = ['Harry Potter', 'Twilight']
    assert len(books) == 2

#this is supposed to test if the title input can be entered as a string
def test_input_of_each_descriptor():
    title = ""
    input = ""
    assert title == input
