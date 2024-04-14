import isbnlib
import pandas as pd

# Function to find ISBN number for a given title
def find_isbn(title):
    try:
        isbn = isbnlib.isbn_from_words(title)         
        return isbn
    except Exception as e:
        print(f"Error finding ISBN for '{title}': {e}")
        return None

# Read the Excel file
excel_file_path = r'C:/Users/YourUserName/Desktop/books.xlsx'  # Update with your file path
df = pd.read_excel(excel_file_path)

# Find ISBN numbers for each title
df['ISBN'] = df['Title'].apply(find_isbn)

# Save the changes to the Excel file
df.to_excel(excel_file_path, index=False)
print("ISBN numbers added to the Excel file.")



