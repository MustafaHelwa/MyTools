# Book ISBN and Info Finder

## Description:
This folder contains a Python script for finding book information based on ISBN (International Standard Book Number). 
The script retrieve details such as book title, author, publication date, and more.

## Features:
- **Name Lookup:** Enter book name to retrieve ISBN book.
- **Details Retrieval:** Obtain details like book title, author, publication date, publisher, and genre.
- **API Integration:** Utilizes online book databases to fetch accurate and up-to-date information.
- **User-friendly Interface:** Simple command-line interface for easy interaction.

## How to Use Manual Finder:
1. Clone or download this repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the directory containing the script.
4. Run the script using Python: `python Book_INFO_Finder_Manual.py` or others.
5. Follow the on-screen instructions to input a book name and retrieve book information.

## How to Use Auto Finder:
1. Clone or download this repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the directory containing the script.
4. Run the script using Python: `python Book_INFO_Finder_Auto.py`.
5. Ensure you have an existing `books.xlsx` file on your desktop (change file path as needed).
6. Keep a separate copy of your original file since this code will overwrite `books.xlsx` data.


## Dependencies:
- Python 3.x
- isbnlib library (Install using `pip install isbnlib` if not already installed)
- pandas library (Install using `pip install pandas` if not already installed)

## File Structure:
- `book_isbn_info_finder.py`: Main Python script for fetching book information.
- `Book_List_Finder_Auto`: Python script for fetchin book information automatically, along with excel files needed.  
- `README.md`: Readme file providing information about the script and usage instructions.

## Credits:
- This script utilizes libraries provided by online book databases for fetching book information.
- By [Mustafa Helwa].
