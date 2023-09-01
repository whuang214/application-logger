import ezsheets


def main():
    # Initialize the ezsheets module (this will prompt for authentication on the first run)
    ezsheets.init()

    # Get the spreadsheet by its ID or URL. Replace with your Spreadsheet ID or URL.
    ss = ezsheets.Spreadsheet("1TE_EkneOkYaK9j7eSOM9i3mga3s1c5XxJFEe6xGvNJg")

    # Get the first sheet
    sheet = ss[0]

    # Print the title of the sheet
    print(sheet.title)


if __name__ == "__main__":
    main()
