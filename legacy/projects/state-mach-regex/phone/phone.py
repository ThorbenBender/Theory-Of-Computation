import re  # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
pattern = r'0\d{10}'

while line != "exit":
    # TODO Find matches
    match = re.findall(pattern, line)
    # TODO If no match found, print that no number was found
    if len(match) == 0:
        print('No number found')
    # # TODO Else, break number up into area code, prefix, and suffic
    else:
        number = match[0]
        print(
            f'Area code: {number[:4]} Prefix: {number[4:8]} Suffix: {number[8:11]}')
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")
