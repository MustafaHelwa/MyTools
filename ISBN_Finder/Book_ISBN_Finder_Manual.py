import isbnlib

def find_isbn(book_title):
    try:
        book_info = isbnlib.goom(book_title)
        if book_info:
            # Extract the ISBN number of the first book
            isbn_number = book_info[0]['ISBN-13']
            return isbn_number
        else:
            return "ISBN not found for this book."
    except Exception as e:
        return f"Error: {e}"

# Example usage:
book_title = input("Enter the title of the book: ")
isbn_number = find_isbn(book_title)
print(f"ISBN for '{book_title}': {isbn_number}")


input("Press enter to exit;")
