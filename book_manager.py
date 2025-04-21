import json

class BookCollection:
    def __init__(self):
        self.storage_file = "books_data.json"
        self.book_list = []
        self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        book_title = input("Enter the title of the book: ")
        book_author = input("Enter the author of the book: ")
        publication_year = input("Enter the publication year of the book: ")
        book_genre = input("Enter the genre of the book: ")
        is_book_read = input("Has the book been read? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")

    def delete_book(self):
        book_title = input("Enter the title of the book to delete: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book deleted successfully!\n")
                return
        print("Book not found in the collection.\n")

    def find_book(self):
        print("Search by:\n1. Title\n2. Author")
        search_type = input("Enter your choice (1 or 2): ").strip()
        search_text = input("Enter search term: ").strip().lower()

        if search_type == "1":
            found_books = [book for book in self.book_list if search_text in book["title"].lower()]
        elif search_type == "2":
            found_books = [book for book in self.book_list if search_text in book["author"].lower()]
        else:
            print("Invalid choice.\n")
            return

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Not Read"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        else:
            print("No matching books found.\n")

    def update_book(self):
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                new_title = input(f"New title ({book['title']}): ").strip()
                new_author = input(f"New author ({book['author']}): ").strip()
                new_year = input(f"New year ({book['year']}): ").strip()
                new_genre = input(f"New genre ({book['genre']}): ").strip()
                read_input = input("Have you read this book? (yes/no): ").strip().lower()

                if new_title:
                    book["title"] = new_title
                if new_author:
                    book["author"] = new_author
                if new_year:
                    book["year"] = new_year
                if new_genre:
                    book["genre"] = new_genre
                if read_input in ["yes", "no"]:
                    book["read"] = read_input == "yes"

                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    def show_all_books(self):
        if not self.book_list:
            print("Your book collection is empty.\n")
            return

        print("Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Not Read"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        print()

    def show_reading_progress(self):
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a New Book")
            print("2. Delete a Book")
            print("3. Find a Book")
            print("4. Update Book details")
            print("5. Show All Books")
            print("6. Show Reading Progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Goodbye! Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
