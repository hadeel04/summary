# Personal Library Manager

The Personal Library Manager is a command-line interface (CLI) application that allows users to manage their book collections. It provides functionality for adding, listing, editing, deleting, searching, and sorting books in a personal library.

## Features

- **Add Book**: Users can add a new book with details such as title, author, publication year, and genre.
- **List Books**: Display all books in the library or filter by author or genre.
- **Edit Book**: Modify the details of an existing book, such as title, author, publication year, or genre.
- **Delete Book**: Remove a book entry from the library.
- **Search Books**: Search for books by title or author using a query string.
- **Sort Books**: Sort the list of books based on title, author, publication year, or genre.
- **Save and Load Library**: The application automatically loads the library from a file on startup and saves any changes to the file before exiting.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/hadeel04/summary.git
    ```

2. Navigate to the project directory:

    ```bash
    cd personal-library-manager
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
 Run the application using the following command:
   
   ```bash
python main.py --file /path/to/custom_library.json
```
The `--file` option allows you to specify the path to the library file. If not provided, the default file `library.json` will be used in the current directory.

Follow the on-screen prompts to perform various operations on your library.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

