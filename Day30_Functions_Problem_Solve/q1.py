# Library system

library = []

def add_book(library, title, author, copies):
    book = {
        "Title": title,
        "Author": author,
        "Copies": copies
    }
    library.append(book)

def show_books(library):
    print("\nLibrary Books:")
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book['Title']} by {book['Author']} - Copies: {book['Copies']}")



N = int(input("Enter number of books: "))

for i in range(N):
    title = input("Title of the book: ")
    author = input("Author Name: ")
    copies = int(input("Copies: "))
    
    add_book(library, title, author, copies)

show_books(library)
