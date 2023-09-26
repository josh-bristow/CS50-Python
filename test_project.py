from project import is_valid_book, add_book_to_read_list, remove_book_from_read_list, view_read_list

# Sample data for testing
sample_book_info = {
    "title": "Sample Book Title",
    "authors": ["Author1", "Author2"],
}
sample_existing_books_ids = set()
sample_read_list_file = "test_read_list.txt"

def test_is_valid_book_valid():
    assert is_valid_book(sample_book_info) is True

def test_is_valid_book_no_title():
    book_info = {"authors": ["Author1"]}
    assert is_valid_book(book_info) is False

def test_is_valid_book_empty_authors():
    book_info = {"title": "Sample Book Title", "authors": []}
    assert is_valid_book(book_info) is False


def test_add_book_to_read_list_existing_book(monkeypatch, capsys):
    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: '0')

    existing_read_list = ["Title: Sample Book Title\n", "Authors: Author1, Author2\n\n"]
    with open(sample_read_list_file, 'w', encoding='utf-8') as file:
        file.writelines(existing_read_list)

    book = {"title": "Sample Book Title", "authors": ["Author1", "Author2"], "id": "123"}
    add_book_to_read_list(book, sample_read_list_file)

    captured = capsys.readouterr()
    assert "Sample Book Title is already in your read list." in captured.out

def test_remove_book_from_read_list_existing_book(monkeypatch, capsys):
    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: '0')

    existing_read_list = ["Title: Sample Book Title\n", "Authors: Author1, Author2\n\n"]
    with open(sample_read_list_file, 'w', encoding='utf-8') as file:
        file.writelines(existing_read_list)

    remove_book_from_read_list(sample_read_list_file)

    with open(sample_read_list_file, 'r', encoding='utf-8') as file:
        updated_read_list = file.readlines()

    assert len(updated_read_list) == 0

def test_view_read_list_empty(capsys):
    view_read_list(sample_read_list_file)
    captured = capsys.readouterr()
    assert "Your read list is empty." in captured.out
