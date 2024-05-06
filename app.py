from book import Book
from library import Library
import argparse


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Personal Library Manager')
    parser.add_argument('--file', type=str, default='library.json', help='Path to the library file (default: '
                                                                         'library.json)')

    # Parse the command-line arguments
    args = parser.parse_args()

    library = Library(args.file)

    while True:
        print("\nPersonal Library Manager")
        print("1. Add Book")
        print("2. List Books")
        print("3. Edit Book")
        print("4. Delete Book")
        print("5. Search Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            if not title.strip():
                print("Book title cannot be empty.")
                continue
            author = input("Enter book author: ")
            year_str = input("Enter publication year: ")
            try:
                year = int(year_str)
            except ValueError:
                print("Invalid year format. Please enter a valid integer.")
                continue
            genre = input("Enter book genre: ")
            book = Book(title, author, year, genre)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            author = input("Enter author (or leave blank for all): ")
            genre = input("Enter genre (or leave blank for all): ")
            library.list_books(author if author else None, genre if genre else None)

        elif choice == "3":
            title = input("Enter book title to edit: ")
            if not title.strip():
                print("Book title cannot be empty.")
                continue
            new_title = input("Enter new title (or leave blank): ")
            new_author = input("Enter new author (or leave blank): ")
            new_year = input("Enter new publication year (or 0): ")
            new_genre = input("Enter new genre (or leave blank): ")
            library.edit_book(title, new_title if new_title.strip() else None,
                              new_author if new_author.strip() else None,
                              new_year if new_year.strip() else None, new_genre if new_genre.strip() else None)

        elif choice == "4":
            title = input("Enter book title to delete: ")
            if not title.strip():
                print("Book title cannot be empty.")
                continue
            library.delete_book(title)

        elif choice == "5":
            query = input("Enter search query , a title of  book or a name of author: ")
            results = library.search_books(query)
            if not results:
                print("No books found matching the search .")
            else:
                print("Search results:")
                for book in results:
                    print(book)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
