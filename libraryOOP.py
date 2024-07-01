class Book:
    author = None
    title = None
    availability = None
    
    def __init__(self, author, title, availability):
        self.author = author
        self.title = title
        self.availability = availability

class Member:
    memberID = None
    firstName = None
    lastName = None 
    borrowedBooks = [] 

    def __init__(self, memberID, firstName, lastName, borrowedBooks):
        self.memberID = memberID
        self.firstName = firstName
        self.lastName = lastName
        self.borrowedBooks = borrowedBooks

class Library:
    books = []
    members = []

    def addBooks(self, bookList):
        self.books += bookList

    def addMembers(self, membersList):
        self.members += membersList

    def lendBooks(self, member, bookList):
        member.borrowedBooks += bookList

    def bookReturn(self, member, book):
        member.borrowedBooks.remove(book)

library = Library()
book = Book('John Smith', 'Finding Hope', True)
member = Member(1234, 'Kat', 'franczak', [book])
library.addBooks([book])
library.addMembers([member])
print(library)
        