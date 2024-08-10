#Creating the super class
class LibraryItem:
    def __init__(self, title, availability=True):
        self.title = title
        self.availability = availability

    def get_details(self):
        return f"Title: {self.title}, Availability: {'Available' if self.availability else 'Not Available'}"

#Creating Sub class
class Book(LibraryItem):
    def __init__(self, title, author, genre, isbn, availability=True):
        super().__init__(title, availability)
        self.author = author
        self.genre = genre
        self.isbn = isbn

    def checkout(self):
        if self.availability:
            self.availability = False
            print("Book checked out")
        else:
            print("Book is already checked out")

    def return_book(self):
        self.availability = True
        print("Book returned")

    def update_availability(self, new_status):
        if not new_status and not self.availability:
            print("Book is currently checked out")
        else:
            self.availability = new_status

    def get_details(self):
        details = super().get_details()
        return f"{details}, Author: {self.author}, Genre: {self.genre}, ISBN: {self.isbn}"

    def add_to_library(self):
        print(f"Book added to library: {self.title}")

# Creating random book objects
book1 = Book("Harry Potter: Philosopher's Stone", "J.k. Rowling", "Fiction", "978-0545069670")
book2 = Book("The Hidden Hindu", "Akshat Gupta", "Fiction", "978-0143455691")

#Calling the functions on book 1
book1.get_details()
book1.checkout()
book1.return_book()
book1.update_availability(False)
book1.add_to_library()

#Calling the functions on book2
book2.get_details()
book2.checkout()
book2.add_to_library()

