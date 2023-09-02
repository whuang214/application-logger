import ezsheets
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Get the spreadsheet ID from environment variables or ask the user
SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
if not SPREADSHEET_ID:
    SPREADSHEET_ID = input("Please enter the spreadsheet ID or link: ")


def main():
    # Initialize the ezsheets module (this will prompt for authentication on the first run)
    ezsheets.init()

    # Get the spreadsheet by its ID or URL. Replace with your Spreadsheet ID or URL.
    ss = ezsheets.Spreadsheet(SPREADSHEET_ID)

    # Get the first sheet
    sheet = ss[0]

    # Print the title of the sheet
    print(sheet.title)

    # Print first row (headers)
    headers = sheet.getRow(1)
    print(headers)


if __name__ == "__main__":
    main()
