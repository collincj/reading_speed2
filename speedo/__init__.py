

# create a function to calculate reading speed
def calc_ppm(pages, minutes):
    return pages/minutes

class Book: #creates Book as a class which can house functions and variables

#Statistics regarding books. The books have the following properties:

#Attributes:
    #pform: the platform of the book.
    #title: the title of the book.
    #pages: how many pages the user read.
    #minutes: how long it took the user to read said pages.
    #books: number of books

    def __init__(self, pform=None, title=None, pages=None, minutes=None, books=None): #has to be matched exactly on the test page
        if pform is None:
            pform = "print" # default platform value
        self.platform = pform # takes special init function and sets it equal to the value that gets passed
        if title is None:
            title = "unknown" #default title value
        self.title = title
        if pages is None:
            pages = 100 #default pages read
        self.pages = pages
        if minutes is None:
            minutes = 100 #default minutes read
        self.minutes = minutes
        if books is None:
            books = 1
        self.books = books

    def ppm(self):
        return self.pages / self.minutes

#an attempt at a Library class
#class Library:
    #books = [] #empty list of books in our Library

    #def addBook(self, Book):
        #self.books.append(book)

    #def contents():
        #for book in self.books:
            #print(book.title + "has " + book.pages + " pages")
    #def pages():
        #for book in self.books:
            #print(book.title + "has " + book.pages + " pages")
