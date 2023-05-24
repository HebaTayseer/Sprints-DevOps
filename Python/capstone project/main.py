from datetime import datetime
import csv
import os.path
from email_validator import validate_email, EmailNotValidError

# Define constants
DATE_FORMAT = "%Y-%m-%d"
FILE_EXTENSION = ".csv"
FIELDNAMES = ['User-name', 'Email', 'Phone number', 'Address']

# Get current date and time
current_date = datetime.now().strftime(DATE_FORMAT)

# Create a file object with current date in the filename
filename = f"ContactBook_{current_date}{FILE_EXTENSION}"

# Check if file already exists
file_exists = os.path.isfile(filename)


def is_unique_username(username):
    """Check if username is unique."""
    if file_exists:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    print("This username is already taken !")
                    return False
    return True


def is_unique_email(email):
    """Check if email is unique."""
    try:
        email = validate_email(email).email
    except EmailNotValidError as e:
        print(str(e))
        return False

    if file_exists:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == email:
                    print("This email already exists !")
                    return False
    return True


def get_phone_number():
    """Get phone number from user and validate it."""
    while True:
        try:
            phone_number = int(input('Please enter your phone number : '))
            if len(str(phone_number)) != 10:
                print('Invalid mobile number.')
            else:
                return phone_number
        except ValueError:
            print('Please enter a valid integer!')


def get_address():
    """Get address from user."""
    return input('Please enter your address : ')


def add_contact():
    """Add a new contact to the file."""
    while True:
        user_name = input('Please enter your username : ')
        if is_unique_username(user_name):
            break

    while True:
        email = input('Please enter your email : ')
        if is_unique_email(email):
            break

    phone_number = get_phone_number()
    address = get_address()

    # save contact information in a list
    row = [user_name, email, phone_number, address]

    # write contact information to file
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(FIELDNAMES)
        writer.writerow(row)
    print('Contact has been added successfully')


def update_contact():
    """Update an existing contact in the file."""
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    print('Contacts:')
    for i, row in enumerate(rows):
        print(f"{i + 1}) {row['Email']}")
    print('0) Exit')

    while True:
        try:
            row_index = int(input('Enter the number of the contact you want to update: '))
            if row_index == 0:
                break
            elif row_index < 1 or row_index > len(rows):
                print('Invalid choice')
                continue
            print('Fields:')
            for i, fieldname in enumerate(FIELDNAMES):
                print(f"{i + 1}) {fieldname}")
            print('0) Exit')
            field_index = int(input('Enter the number of the field you want to update: '))
            if field_index == 0:
                break
            elif field_index < 1 or field_index > len(FIELDNAMES):
                print('Invalid choice')
                continue
            new_value = input(f'Enter the new {FIELDNAMES[field_index - 1]}: ')
            rows[row_index - 1][FIELDNAMES[field_index- 1]] = new_value
            break
        except ValueError:
            print('Please enter a valid integer!')

    # write updated contact information to file
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print('Contact has been updated successfully')


def delete_contact():
    """Delete an existing contact from the file."""
    email = input('Enter the email for the contact you want to delete: ')
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    row_deleted = False
    for i, row in enumerate(rows):
        if row[1] == email:
            rows.pop(i)
            row_deleted = True
            break
    if not row_deleted:
        print("This email doesn't exist in the file!")
        return

    # write updated contact information to file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
    print('Contact has been deleted successfully')


# Main loop
while True:
    print('Menu:')
    print('1) Add Contact')
    print('2) Update Contact')
    print('3) Delete Contact')
    print('0) Exit')
    choice = input('Please enter the number of your choice: ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '0':
        break
    else:
        print('Please enter a valid number.')
