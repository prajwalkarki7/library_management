books = {}
users = []

def register():
    name = input("Enter your name: ")
    password = input("Enter a password: ")
    users.append({"name": name, "password": password})
    print("Record successfully added")
    login()

def login():
    users_name = input("Enter your name: ")
    users_pass = input("Enter your password: ")
    for user in users:
        if user['name'] == users_name and user['password'] == users_pass:
            print("Login successfully")
            main()
            return
    print("Incorrect ID or password")

def main():
   while True:
        try:
            choice = int(input("Enter the choice you want to choose:\n 1. Add Book\n 2. Display Books\n 3. Search Book\n 4. Delete Book\n 5. Update Book\n 6. Check Out Book\n 7. Check In Book\n 8. Exit\n"))
            if choice == 1:
                addbooks()
            elif choice == 2:
                displaybook()
            elif choice == 3:
                searchbook()
            elif choice == 4:
                removebook()
            elif choice == 5:
                updatebook()
            elif choice == 6:
                checkoutbook()
            elif choice == 7:
                checkinbook()
            elif choice == 8:
                print("Exiting...")
                break
            else:
                print("Incorrect choice")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 8.")

def addbooks():
    try:
        book_id = input("Enter your book id number: ")
        book_name = input("Enter the book name: ")
        book_author = input("Enter the book author name: ")
        books[book_id] = {'book_name': book_name, 'book_author': book_author, 'checked_out': False}
        print("Book added successfully")
    except Exception as e:
        print(f"An error occurred while adding the book: {e}")
def displaybook():
    if not books:
        print("\nNo records to display.")
    else:
        print("\nRecords:")
        for book_id, details in books.items():
            print(f"Book ID: {book_id}")
            print(f"  Book Name: {details['book_name']}")
            print(f"  Book Author: {details['book_author']}")
            print(f"  Checked Out: {'Yes' if details['checked_out'] else 'No'}")
            print("-" * 30)

def searchbook():
    x = input("Enter the book number you want to search: ")
    if x in books:
        print("\nDetails are:")
        print(f"Book ID: {x}")
        print(f"  Book Name: {books[x]['book_name']}")
        print(f"  Book Author: {books[x]['book_author']}")
        print(f"  Checked Out: {'Yes' if books[x]['checked_out'] else 'No'}")
    else:
        print("\nNo record found with that book number.")

def removebook():
    y = input("Enter the book number you want to delete: ")
    if y in books:
        books.pop(y)
        print("Deleted successfully")
    else:
        print("\nNo such ID found")

def updatebook():
    book_id = input("Enter the book number you want to update: ")
    if book_id in books:
        book_name = input("Enter the new book name: ")
        book_author = input("Enter the new book author name: ")
        books[book_id]['book_name'] = book_name
        books[book_id]['book_author'] = book_author
        print("Book details updated successfully")
    else:
        print("\nNo record found with that book number.")

def checkoutbook():
    book_id = input("Enter the book number you want to check out: ")
    if book_id in books:
        if books[book_id]['checked_out']:
            print("This book is already checked out.")
        else:
            books[book_id]['checked_out'] = True
            print("Book checked out successfully")
    else:
        print("\nNo record found with that book number.")

def checkinbook():
    book_id = input("Enter the book number you want to check in: ")
    if book_id in books:
        if not books[book_id]['checked_out']:
            print("This book is already checked in.")
        else:
            books[book_id]['checked_out'] = False
            print("Book checked in successfully")
    else:
        print("\nNo record found with that book number.")

register()
