library = []
def main():
    pass  
if __name__ == "__main__":
    main()
library = []

def add_book():
    print("--- Enter book information ---")
    book_id = input("Enter the book code: ")
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    
    book = {
        "id": book_id,
        "title": title,
        "author": author
    }
    
    library.append(book)
    print(f"Books added '{title}' entered the library successfully!")

def main():
    add_book() 
if __name__ == "__main__":
    main()

def view_books():
    print("\n--- List of books in the library ---")
    if not library:
        print("The library currently has no books.")
    else:
        for book in library:
            print(f"Code: {book['id']} - Name: {book['title']} - Author: {book['author']}")

def main():
    add_book()
    view_books()

if __name__ == "__main__":
    main()