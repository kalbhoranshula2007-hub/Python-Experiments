class Library:
    def __init__(self, book_name, author,available):
        self.book_name = book_name
        self.author = author
        self.available = True

    def checkout_book(self):
        if self.available:
            self.available = False
            print(f"{self.book_name} has been checked out.")
        else:
            print(f"{self.book_name} is currently not available.")

    def return_book(self):
        self.available = True
        print(f"{self.book_name} has been returned and is now available.")

    def display_book(self):
        status = "Available" if self.available else "Not Available"
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)
        print("--------------------")

book1 = Library("Python Basics" , "Guido van Rossum" , True)
book2 = Library("Data Structures" , "Mark Allen Weiss" , False)

book1.display_book()
book2.display_book()

book1.checkout_book()
book1.display_book()

book1.return_book()
book1.display_book()