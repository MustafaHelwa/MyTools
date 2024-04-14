import isbnlib
import pandas as pd

# Function to find book information for a given title
def find_book_info(title):
    try:
        book_info = isbnlib.goom(title)
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
            return {
                'Title': '',
                'Authors': '',
                'Publisher': '',
                'Year': '',
                'Language': '',
                'ISBN': 'ISBN not found'
            }
    except Exception as e:
        print(f"Error finding information for '{title}': {e}")
        return {
            'Title': '',
            'Authors': '',
            'Publisher': '',
            'Year': '',
            'Language': '',
            'ISBN': 'Error'
        }

# Read the Excel file
excel_file_path = r'C:/Users/theth/Desktop/books.xlsx'  # Update with your file path

try:
    df = pd.read_excel(excel_file_path)
except FileNotFoundError:
    print(f"Error: File '{excel_file_path}' not found.")
    exit()

# Find book information for each title
df['Book_Info'] = df['Title'].apply(find_book_info)

# Extract individual columns from the book information dictionary
df['Title'] = df['Book_Info'].apply(lambda x: x['Title'])
df['Authors'] = df['Book_Info'].apply(lambda x: x['Authors'])
df['Publisher'] = df['Book_Info'].apply(lambda x: x['Publisher'])
df['Year'] = df['Book_Info'].apply(lambda x: x['Year'])
df['Language'] = df['Book_Info'].apply(lambda x: x['Language'])
df['ISBN'] = df['Book_Info'].apply(lambda x: x['ISBN'])

# Drop the 'Book_Info' column as it's no longer needed
df = df.drop(columns=['Book_Info'])

# Save the changes to the Excel file
df.to_excel(excel_file_path, index=False)
print("Book information added to the Excel file.")



