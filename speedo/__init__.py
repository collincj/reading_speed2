

# create a function to calcualte reading speedo
def calc_ppm(pages, minutes):
    return pages/minutes

class Book: #creates Book as a class which can house functions and variables

    def __init__(self, pform=None, title=None, pages=None, minutes=None): #has to be matched exactly on the test page
        if pform is None:
            pform = "print" # default platform value
        self.platform = pform # takes special init function and sets it equal to the value that gets passed in
        if title is None:
            title = "unknown"
        self.title = title
        if pages is None:
            pages = 100
        self.pages = pages
        if minutes is None:
            minutes = 100
        self.minutes = minutes

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
