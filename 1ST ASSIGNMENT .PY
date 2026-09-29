class Book:
    def __init__(self, book_no, book_name, writer):
        self.book_no = book_no
        self.book_name = book_name
        self.writer = writer
        self.borrowed = False

    def display(self):
        availability = "Borrowed" if self.borrowed else "Available"
        print(f"ID: {self.book_no}, Title: {self.book_name}, "
              f"Author: {self.writer}, Status: {availability}")


class Patron:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.issued_books = []

    def display(self):
        print(f"Patron ID: {self.member_id}, Name: {self.member_name}")
        if self.issued_books:
            print("Borrowed Books:", ", ".join(self.issued_books))
        else:
            print("No books borrowed.")


class Library:
    def __init__(self):
        self.book_list = {}
        self.member_list = {}

    def add_book(self, new_book):
        self.book_list[new_book.book_no] = new_book
        print(f"Book '{new_book.book_name}' added successfully.")

    def register_patron(self, new_member):
        self.member_list[new_member.member_id] = new_member
        print(f"Patron '{new_member.member_name}' registered successfully.")

    def borrow_book(self, member_id, book_no):
        if member_id not in self.member_list:
            print("Patron not found.")
            return

        if book_no not in self.book_list:
            print("Book not found.")
            return

        selected_book = self.book_list[book_no]
        selected_member = self.member_list[member_id]

        if selected_book.borrowed:
            print(f"Book '{selected_book.book_name}' is already borrowed.")
        else:
            selected_book.borrowed = True
            selected_member.issued_books.append(selected_book.book_name)
            print(f"{selected_member.member_name} borrowed '{selected_book.book_name}'.")

    def return_book(self, member_id, book_no):
        if member_id not in self.member_list:
            print("Patron not found.")
            return

        if book_no not in self.book_list:
            print("Book not found.")
            return

        selected_book = self.book_list[book_no]
        selected_member = self.member_list[member_id]

        if selected_book.book_name in selected_member.issued_books:
            selected_member.issued_books.remove(selected_book.book_name)
            selected_book.borrowed = False
            print(f"{selected_member.member_name} returned '{selected_book.book_name}'.")
        else:
            print(f"{selected_member.member_name} has not borrowed '{selected_book.book_name}'.")

    def display_books(self):
        print("\nLibrary Books:")
        for selected_book in self.book_list.values():
            selected_book.display()

    def display_patrons(self):
        print("\nRegistered Patrons:")
        for selected_member in self.member_list.values():
            selected_member.display()
            print("-" * 30)


lib = Library()

lib.add_book(Book(101, "Python Programming", "John Smith"))
lib.add_book(Book(102, "Data Structures", "Alice Brown"))
lib.add_book(Book(103, "Machine Learning", "Andrew Ng"))

lib.register_patron(Patron(1, "Rahul"))
lib.register_patron(Patron(2, "Sneha"))

lib.display_books()

print("\nBorrowing Books:")
lib.borrow_book(1, 101)
lib.borrow_book(2, 102)

lib.display_books()

print("\nReturning Book:")
lib.return_book(1, 101)

lib.display_books()

lib.display_patrons()