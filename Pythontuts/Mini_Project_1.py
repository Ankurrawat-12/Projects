# Python Mini Project #1
"""
Create a library class
display book
lend book - (who owns the book if not present )
add book
return book
AnkurLibrary = Library(listOfBooks, libraryName)

dictionary -> key -> BookName , value -> NameOfPerson

create a main function and run an infinite
while loop asking users for their input
"""


class Library:
    def __init__(self, list_of_books, library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No reader have lend this book
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = reader
                print("Book Lend")
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self, book, reader):
        if book in self.list_of_books:
            if (self.lend_data[book] is not None) and self.lend_data[book] is reader:
                self.lend_data.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)


def main():
    # By default variables
    list_books = ['Naruto', 'Sherlock Holmes', 'Harry Potter', 'Rich Dad and Poor Dad']
    library_name = 'Ankur'
    secret_key = 123456

    ankur = Library(list_books, library_name)

    _exit = False
    while _exit is not True:
        print(
            f"\nWelcome To {ankur.library_name} library\nq for exit \n"
            f"Display Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \n"
            f"Add Book Using 'a' and Delete Book using 'del' \n ")

        _input = input("option:") 
        print("\n")

        if _input == "q":
            _exit = True

        elif _input == "d":
            ankur.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")

            ankur.lend_book(_input3, _input2)

        elif _input == "a":
            _input2 = input("Book name:")
            ankur.add_book(_input2)

        elif _input == "del":
            _input_secret = int(input("Write the secret key to delete:"))
            if _input_secret == secret_key:
                _input2 = input("Book Which you want to delete:")
                ankur.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            ankur.return_book(_input3, _input2)


if __name__ == "__main__":
    main()
