def add_book(inventory, book_title):
    if book_title in inventory:
        print(f"'{book_title}' is already in the inventory.")
    else:
        inventory[book_title] = None  # None means the book is available
        print(f"'{book_title}' has been added to the inventory.")

def borrow_book(inventory, book_title, borrower_name):
    if book_title not in inventory:
        print(f"'{book_title}' is not in the inventory.")
    elif inventory[book_title] is None:
        inventory[book_title] = borrower_name
        print(f"'{book_title}' has been borrowed by {borrower_name}.")
    else:
        print(f"Sorry, '{book_title}' is already borrowed by {inventory[book_title]}.")

def return_book(inventory, book_title):
    if book_title not in inventory:
        print(f"'{book_title}' is not in the inventory.")
    elif inventory[book_title] is None:
        print(f"'{book_title}' is already available in the library.")
    else:
        inventory[book_title] = None
        print(f"'{book_title}' has been returned and is now available.")

def check_availability(inventory, book_title):
    if book_title not in inventory:
        print(f"'{book_title}' is not in the inventory.")
    elif inventory[book_title] is None:
        print(f"'{book_title}' is available for borrowing.")
    else:
        print(f"'{book_title}' is currently borrowed by {inventory[book_title]}.")

def main():
    inventory = {}

    while True:
        print("\nLibrary Menu:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Check availability")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            book_title = input("Enter the title of the book to add: ").strip()
            add_book(inventory, book_title)
        elif choice == '2':
            book_title = input("Enter the title of the book to borrow: ").strip()
            borrower_name = input("Enter the borrower's name: ").strip()
            borrow_book(inventory, book_title, borrower_name)
        elif choice == '3':
            book_title = input("Enter the title of the book to return: ").strip()
            return_book(inventory, book_title)
        elif choice == '4':
            book_title = input("Enter the title of the book to check: ").strip()
            check_availability(inventory, book_title)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

