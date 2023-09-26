import requests
import random
import os

API_KEY = "Enter Google Books API Key here"
BASE_URL = "https://www.googleapis.com/books/v1/volumes"
READ_LIST_FILE = "My Books.txt"

def main():
    existing_books_ids = set()

    create_read_list_file(READ_LIST_FILE)  # Create the file if it does not exist

    while True:
        try:
            print("Options:")
            print("1. View Random Books and Add to Read List")
            print("2. View Read List")
            print("3. Remove Book from Read List")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                random_books = get_random_books(existing_books_ids)
                if not random_books:
                    print(
                        "No random books available. Please choose option 1 to fetch random books."
                    )
                else:
                    for i, book in enumerate(random_books, start=1):
                        print(f"{i}. Title: {book['title']}")
                        print(f"   Authors: {', '.join(book['authors'])}\n")

                    while True:
                        try:
                            book_choice = int(
                                input(
                                    "Enter the number of the book you want to add to your read list (or 0 to return to the main menu): "
                                )
                            )
                            if book_choice == 0:
                                break
                            elif 1 <= book_choice <= len(random_books):
                                selected_book = random_books[book_choice - 1]
                                add_book_to_read_list(selected_book, "My Books.txt")
                            else:
                                print("Invalid choice. Please enter a valid book number.")
                        except ValueError:
                            print(
                                "Invalid input. Please enter a valid book number or 0 to return to the main menu."
                            )
            elif choice == 2:
                view_read_list("My Books.txt")
            elif choice == 3:
                remove_book_from_read_list("My Books.txt")
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid option.")

def create_read_list_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass  # Create an empty file

def is_valid_book(book_info):
    # Check if the book has a valid title and authors
    title = book_info.get("title", "")
    authors = book_info.get("authors", [])

    # Check if the title contains at least one English letter (to filter out non-English titles)
    if not any(char.isalpha() for char in title):
        return False

    # Check if the authors list is not empty
    if not authors:
        return False

    return True

def get_random_books(existing_books_ids):
    random_books = []
    while len(random_books) < 5:
        # Generate a random start index for pagination
        start_index = random.randint(1, 1000)

        params = {
            "q": "a",
            "startIndex": start_index,
            "maxResults": 5,  # Number of books to retrieve
            "key": API_KEY,
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            for item in data.get("items", []):
                book_id = item.get("id")
                if book_id not in existing_books_ids:
                    volume_info = item.get("volumeInfo", {})
                    if is_valid_book(volume_info):
                        title = volume_info.get("title", "Unknown Title")
                        authors = volume_info.get("authors", ["Unknown Author"])
                        random_books.append(
                            {"title": title, "authors": authors, "id": book_id}
                        )
                        existing_books_ids.add(book_id)
                        if len(random_books) >= 5:
                            return random_books
        else:
            print(f"Error: {response.status_code}")
    return random_books

def add_book_to_read_list(book, read_list_file):
    with open(read_list_file, "r", encoding="utf-8") as file:
        read_list = file.readlines()

    # Check if the book is already in the read list
    for i in range(0, len(read_list), 3):
        if book["title"] in read_list[i]:
            print(f"{book['title']} is already in your read list.")
            return  # Exit the function immediately

    # If the book is not in the read list, add it
    with open(read_list_file, "a", encoding="utf-8") as file:
        file.write(f"Title: {book['title']}\n")
        file.write(f"Authors: {', '.join(book['authors'])}\n\n")

    # Print the success message
    print(f"{book['title']} added to your read list.")

def remove_book_from_read_list(read_list_file):
    with open(read_list_file, "r", encoding="utf-8") as file:
        read_list = file.readlines()

    if not read_list:
        print("-------------------------\nYour read list is empty.\n-------------------------")
        return

    print("Your Read List:")
    for i, line in enumerate(read_list):
        print(f"{i // 3 + 1}. {line.strip()}")

    try:
        book_to_remove = int(
            input(
                "Enter the number of the book you want to remove (or 0 to remove all books or -1 to cancel): "
            )
        )
        if book_to_remove == -1:
            pass  # Cancel operation
        elif book_to_remove == 0:
            with open(read_list_file, "w", encoding="utf-8") as file:
                file.truncate(0)
            print("All books removed from your read list.")
        elif book_to_remove > 0 and book_to_remove < len(read_list) // 3:
            with open(read_list_file, "w", encoding="utf-8") as file:
                for i in range(len(read_list) // 3):
                    if i != book_to_remove - 1:
                        file.write(read_list[i * 3])
                        file.write(read_list[i * 3 + 1])
                        file.write(read_list[i * 3 + 2])
            print("Book removed from your read list.")
        else:
            print("Invalid choice. Please enter a valid book number.")
    except ValueError:
        print(
            "Invalid input. Please enter a valid book number, 0 to remove all books, or -1 to cancel."
        )

def view_read_list(read_list_file):
    with open(read_list_file, "r", encoding="utf-8") as file:
        read_list = file.read()
        if read_list:
            print("---------------\nYour Read List:\n---------------")
            print(read_list)
        else:
            print("-------------------------\nYour read list is empty.\n-------------------------")

if __name__ == "__main__":
    main()
    