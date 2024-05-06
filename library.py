import json
import os

from book import Book


class Library:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = []
        self.load()

    def add_book(self, book):
        self.books.append(book)
        self.save()

    def list_books(self, author=None, genre=None):
        for book in self.books:
            if (author is None or book.author == author) and (genre is None or book.genre == genre):
                print(book)

    def edit_book(self, title, new_title=None, new_author=None, new_year=None, new_genre=None):
        book_found = False
        for book in self.books:
            if book.title == title:
                book_found = True
                if new_title is not None and new_title.strip() == "":
                    print("\nBook title cannot be empty.")
                else:
                    if new_title is not None:
                        book.title = new_title
                if new_author is not None:
                    book.author = new_author
                if new_year is not None:
                    try:
                        book.year = int(new_year)
                    except ValueError:
                        print("\nInvalid year format. Please enter a valid integer.")
                        return
                if new_genre is not None:
                    book.genre = new_genre
                self.save()
                print("\nBook updated successfully!")
                return
        if not book_found:
            print(f"\nNo book found with the title '{title}'")

    def delete_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                del self.books[i]
                self.save()
                print("\nBook deleted successfully!")
                return
        print(f"\nNo book found with the title '{title}'")

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results

    def sort_books(self, key):
        if key == "title":
            return sorted(self.books, key=lambda book: book.title.lower())
        elif key == "author":
            return sorted(self.books, key=lambda book: book.author.lower())
        elif key == "year":
            return sorted(self.books, key=lambda book: book.year)
        elif key == "genre":
            return sorted(self.books, key=lambda book: book.genre.lower())
        else:
            return self.books

    def get_all_books(self):
        return self.books

    def save(self):
        with open(self.file_path, "w") as file:
            data = [vars(book) for book in self.books]
            json.dump(data, file, indent=4)

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]
