  # Bookshelf Buddy
    #### Video Demo:  https://www.youtube.com/watch?v=tdUvn9LJJt8
    #### Description:

    Bookshelf Buddy is a Python script that offers assistance in managing and organizing your reading list. With Bookshelf Buddy you can discover a variety of books add them to your reading list to view the contents of your reading list and even remove books from it. The aim of this project is to simplify the process for book enthusiasts when it comes to curating their reading lists and keeping track of books they wish to read.

    project.py
    This is the main script that contains the core functionality of the Bookshelf Buddy project. It includes the following features:

    View Random Books and Add to Read List: You can explore a list of random books retrieved from the Google Books API. You have the option to add any of these books to your reading list.

    View Read List: You can view your reading list, which is stored in a file named "My Books.txt." The script displays the titles and authors of the books in your list.

    Remove Book from Read List: You can remove a book from your reading list. You can choose to remove a specific book or clear your entire reading list.

    Exit: This option allows you to exit the script.

    My Books.txt
    This file is created and managed by the script. It serves as your reading list. Each book you add to your list is stored in this file with the title and authors.

    requirements.txt
    This file lists the Python dependencies required to run the script. You can install these dependencies using the following command:

    pip install -r requirements.txt

    Design Choices
    Creating "My Books.txt" on First Run
    To ensure a seamless experience for users, I added a function in the project.py script to create the "My Books.txt" file if it does not exist. This design choice eliminates the risk of encountering a FileNotFoundError when selecting option 2 (View Read List) on the first run of the script.

    User-Friendly Menu Interface
    I implemented a menu-driven interface to make the script user-friendly. Users can easily choose their desired option by entering the corresponding number.  The script also handles invalid inputs gracefully, providing clear prompts and error messages.

    Random Book Retrieval
    The script fetches a list of random books from the Google Books API by making requests with a random start index. This design choice adds an element of surprise and variety when users explore new books to add to their reading list.