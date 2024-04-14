import isbnlib

def find_book_info(book_title):
    try:
        book_info = isbnlib.goom(book_title)
        if book_info:
            # Extract information of the first book
            book_data = {
                'Title': book_info[0].get('Title', ''),
                'Authors': book_info[0].get('Authors', ''),
                'Publisher': book_info[0].get('Publisher', ''),
                'Year': book_info[0].get('Year', ''),
                'Language': book_info[0].get('Language', ''),
                'ISBN': book_info[0].get('ISBN-13', 'ISBN not found')
            }
            return book_data
        else:
            return "Information not found for this book."
    except Exception as e:
        return f"Error: {e}"

# Example usage:
book_title = input("Enter the title of the book: ")
book_info = find_book_info(book_title)

print("\nInformation for '{}':".format(book_title), end = "\n")
for key, value in book_info.items():
    print(f"{key}: {value}")

input("\nPress enter to exit...\n")