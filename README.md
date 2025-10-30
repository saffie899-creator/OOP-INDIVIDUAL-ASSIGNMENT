[Readme.py](https://github.com/user-attachments/files/23240226/Readme.py)
def print_readme():
    readme_text = """
Mini Library Management System

Project Overview:
This project is a simple Library Management System built in Python.
It uses lists, dictionaries, and tuples to manage books, members, and genres.
The system supports adding, searching, updating, deleting, borrowing, and returning books.

Features and Requirements:

Data Structures
- Books: Stored in a dictionary with ISBN as key; values include title, author, genre, and total copies.
- Members: Stored as a list of dictionaries with member ID, name, email, and borrowed books.
- Genres: Stored as a tuple containing valid genres (e.g., Fiction, Non-Fiction, Sci-Fi).

Core Functions (CRUD + Borrow/Return)
- add_book() — Adds a book if ISBN is unique and genre is valid.
- add_member() — Adds a member if ID is unique.
- search_books() — Search by book title or author.
- update_book() / update_member() — Update book or member details.
- delete_book() / delete_member() — Deletes only if no borrowed items.
- borrow_book() — Allows member to borrow up to 3 books if available.
- return_book() — Return borrowed books.

Documentation:
- A UML diagram (hand-drawn) showing data structures and functions is included.
- A design rationale (1-2 pages) explains why dictionaries, lists, and tuples were used.

Submission:
- operations.py — Core functions implementation
- demo.py — Demo script showing system usage
- tests.py — Unit tests using asserts
- UML diagram image/pdf
- Design rationale PDF
- This README content

Contact:
Prepared by: Amadus Coker
Course: PROG211 Object-Oriented Programming 1
Institution: Limkokwing University of Creative Technology
"""
    print(readme_text)

if __name__ == "__main__":
    print_readme()
