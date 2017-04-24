#import pytest for testing framework
import pytest
import inspect

#import the code we're testing
from speedo import *

#smoke test
def test_smoke():
    assert True

def test_it_can_calculate_ppm():
    pages_read = 100 # number of pages
    time_spent = 180 # minutes spent reading
    assert calc_ppm(pages_read, time_spent) == 100/180
    assert calc_ppm(200, 50) == 4

def test_book_class_exists():
    assert inspect.isclass(Book)

def test_it_can_create_a_book_instance():
    harry_potter = Book()
    assert isinstance(harry_potter, Book)

def test_a_book_has_a_platform():
    harry_potter = Book("print")
    twilight = Book("ebook")
    assert hasattr(harry_potter, "platform") # Check that the property exists
    assert harry_potter.platform == "print" # and that is has the expected value
    assert twilight.platform == "ebook" # and that it can be set to something els


def test_a_book_and_report_ppm():
    assert harry_potter = Book("print", "Harry Potter")
    assert harry_potter.ppm() == 1

def test_an_array_of_books():
    harry_potter = Book("print", "Harry potter")
    books = []
    books.append(harry_potter)
    assert len(books) == 1
