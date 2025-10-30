# operations.py

# Data structures
books = {}  # ISBN -> {title, author, genre, total_copies, available_copies}
members = []  # List of dicts: {member_id, name, email, borrowed_books}
genres = ("Fiction", "Non-Fiction", "Sci-Fi")

# ------------- CORE FUNCTIONS -------------

def add_book(isbn, title, author, genre, total_copies):
    """Add a book if ISBN is unique and genre is valid."""
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return "Book added successfully."

def add_member(member_id, name, email):
    """Add a member if ID is unique."""
    for m in members:
        if m["member_id"] == member_id:
            return "Member already exists."
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return "Member added successfully."

def search_book(keyword):
    """Search book by title or author."""
    results = []
    for isbn, info in books.items():
        if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower():
            results.append((isbn, info))
    return results

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    """Update book details."""
    if isbn not in books:
        return "Book not found."
    if genre and genre not in genres:
        return "Invalid genre."
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if total_copies:
        diff = total_copies - books[isbn]["total_copies"]
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available_copies"] += diff
    return "Book updated successfully."

def delete_book(isbn):
    """Delete a book."""
    if isbn not in books:
        return "Book not found."
    del books[isbn]
    return "Book deleted successfully."

def delete_member(member_id):
    """Delete member if they have no borrowed items."""
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                return "Cannot delete member with borrowed books."
            members.remove(m)
            return "Member deleted successfully."
    return "Member not found."

def borrow_book(member_id, isbn):
    """Borrow a book if available and member has <3 books."""
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return "Borrowing limit reached."
            if isbn not in books:
                return "Book not found."
            if books[isbn]["available_copies"] <= 0:
                return "No copies available."
            books[isbn]["available_copies"] -= 1
            m["borrowed_books"].append(isbn)
            return "Book borrowed successfully."
    return "Member not found."

def return_book(member_id, isbn):
    """Return borrowed book."""
    for m in members:
        if m["member_id"] == member_id:
            if isbn not in m["borrowed_books"]:
                return "Book not borrowed by member."
            m["borrowed_books"].remove(isbn)
            books[isbn]["available_copies"] += 1
            return "Book returned successfully."
    return "Member not found."