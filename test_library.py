# tests.py# tests.py
# # Unit tests for Library Management System using assert statements
#
# from operations import (
#     add_book,
#     add_member,
#     borrow_book,
#     return_book,
#     delete_book,
#     get_book_info
# )
#
# def run_tests():

#     # Setup initial empty records
#     # ---------------------------
#     books = {}
#     members = {}
#
#
#     # Test 1: Add a book
#
#     add_book(books, "B001", "Python Programming", 3)
#     assert "B001" in books, "Book was not added"
#     assert books["B001"]["title"] == "Python Programming"
#     assert books["B001"]["copies"] == 3
#
#     # ---------------------------
#     # Test 2: Add a member
#     # ---------------------------
#     add_member(members, "M001", "Alice")
#     assert "M001" in members, "Member was not added"
#     assert members["M001"]["name"] == "Alice"
#
#     # ---------------------------
#     # Test 3: Borrow a book
#     # ---------------------------
#     borrow_book(books, "B001")
#     assert books["B001"]["copies"] == 2, "Book copy count not reduced after borrow"
#
#     # ---------------------------
#     # Test 4: Borrow a book until no copies left
#     # ---------------------------
#     borrow_book(books, "B001")
#     borrow_book(books, "B001")
#     try:
#         borrow_book(books, "B001")  # Should raise an error
#     except ValueError as e:
#         assert str(e) == "No copies left to borrow.", "Wrong error message for no copies left"
#
#     # ---------------------------
#     # Test 5: Return a book
#     # ---------------------------
#     return_book(books, "B001")
#     assert books["B001"]["copies"] == 1, "Book copies not updated after return"
#
#     # ---------------------------
#     # Test 6: Get book info
#     # ---------------------------
#     info = get_book_info(books, "B001")
#     assert info["title"] == "Python Programming"
#     assert info["copies"] == 1
#
#     # ---------------------------
#     # Test 7: Delete a book
#     # ---------------------------
#     delete_book(books, "B001")
#     assert "B001" not in books, "Book was not deleted"
#
#     print(" All tests passed successfully!")
#
#
# if __name__ == "__main__":
#     run_tests()
