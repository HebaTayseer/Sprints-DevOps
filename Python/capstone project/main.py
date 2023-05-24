# import modules
from datetime import datetime
import csv
from email_validator import validate_email, EmailNotValidError
import os.path

# get current date and time
current_date = datetime.now().strftime("%Y-%m-%d")
# convert datetime obj to string
str_current_date = str(current_date)
# create a file object along with extension
file_name = "ContactBook_" + str_current_date + ".csv"


# This function reads contacts information from user and validate them
# then send them to the writer function.
def contact_info():
    # reading username from the user
    while True:
        user_name = input('Please enter your username : ')
        # checking if the csv file exists or not
        path = f'./ContactBook_{str_current_date}.csv'
        check_file = os.path.isfile(path)
        # checking whether this username is used or not
        if check_file:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)
            for row in rows:
                if row[0] == user_name:
                    print("This username is already taken !")
                    break
            else:
                break
        else:
            break

    while True:
        email = input('Please enter your email : ')
        try:
            email = validate_email(email).email
            # checking if the file already exists
            if check_file:
                # checking if the email already exists
                with open(file_name, 'r') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                for row in rows:
                    if row[1] == email:
                        print("This email already exists !")
                        break
                else:
                    break
            else:
                break
        except EmailNotValidError as e:
            print(str(e))

    # reading the phone numer
    while True:
        # validating that all entries are integer numbers
        try:
            phone_number = int(input('Please enter your phone number : '))
            # validating that the number consists of 10 digits
            if len(str(phone_number)) != 10:
                print('Invalid mobile number.')
            else:
                break
        # validate that the user entered an integer
        except ValueError:
            print('Please enter a valid integer!')
    # reading the address
    address = input('Please enter your address : ')

    # saving contact information in a list
    rows = [[user_name, email, phone_number, address]]
    # field names
    fields = ['User-name', 'Email', 'Phone number', 'Address']
    # calling the writer function to save contact information in the file.
    writer(fields, rows, file_name, "write")


# This function saves contact information in the csv file and updates the existed ones.
def writer(header, data, filename, option):
    if option == "write":
        path = f'./ContactBook_{str_current_date}.csv'
        check_file = os.path.isfile(path)
        # Checking if the file exists so we write column names once.
        if not check_file:
            with open(filename, "w", newline="") as csvfile:
                m = csv.writer(csvfile)
                m.writerow(header)
                for x in data:
                    m.writerow(x)
                    print('Contact has been added successfully')
        # If file already exists do not rewrite column names
        else:
            with open(filename, "a", newline="") as csvfile:
                movies = csv.writer(csvfile)
                for x in data:
                    movies.writerow(x)
                    print('Contact is added successfully')

    # updating existed contacts
    elif option == "update":
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
            print('Contact has been updated successfully')

    else:
        print("Option is not known")


# This function updates existed contacts
def update():
    with open(file_name, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        # choosing the number of field and row user wants to update.
        while True:
            print('fields = [1)User-name, 2)Email, 3)Phone number, 4)Address 0)exit]')

            try:
                n = int(input('Please enter the number of the field you want to update or enter 0 to exit : '))
                with open(f"./{file_name}", 'r') as file:
                    csvreader = csv.reader(file)
                    for row in csvreader:
                        print(row)
                x = int(input('Please enter the number of the row you want to update : '))
                if n == 1:
                    readData[x]['User-name'] = input('Please enter the new username : ')
                    print(readData[x])
                    break
                elif n == 2:
                    readData[x]['Email'] = input('Please enter the new email: ')
                    print(readData[x])
                    break
                elif n == 3:
                    readData[x]['Phone number'] = input('Please enter the new phone number : ')
                    print(readData[x])
                    break
                elif n == 4:
                    readData[x]['Address'] = input('Please enter the new Address : ')
                    print(readData[x])
                    break
                elif n == 0:
                    break

                else:
                    print('Invalid choice')
            except Exception as error:
                print(error)

    readHeader = readData[x].keys()
    # Calling the writer function to write updates to the file.
    writer(readHeader, readData, file_name, "update")


# This function deletes existed contacts using emails
def delete():
    search_email = input("Enter The Email for the contact You Want To delete: ")

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        print(rows)
    for row in rows:
        if row[1] == search_email:
            rows.remove(row)
            with open(file_name, 'w', newline='') as file:
                adder = csv.writer(file)
                adder.writerows(rows)
            print("Contact has been  deleted Successfully")
            break
    else:
        print("This Email doesn't exist in the file !")


# calling functions according to user choice.
Choices = ['1) Add Contact', '2) Update Contact', '3) Delete Contact', '0) exit']
while True:
    for i in Choices:
        print(i)
    choice = input('Please enter the number of your choice : ')
    if choice == '1':
        contact_info()
    elif choice == '2':
        update()
    elif choice == '3':
        delete()
    elif choice == '0':
        break
    else:
        print('Please enter valid number : ')
