# This function checks if the year is a leap year or not.
def leap_year():
    while True:
        try:
            # reads the year  that the user wants to check if it is a leap year.
            year = int(input("Enter the year you want to check if it is a leap year: "))
        # validate that the user entered an integer
        except ValueError:
            print('Please enter a valid integer!')
        # Checks if the year is a leap year.
        else:
            if year % 4 == 0 and year % 100 != 0:
                print(True)
            elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                print(True)
            else:
                print(False)

            # checks if the user wants to check another year
            another_try = input("Do you want to check another year ? (y/n) ")
            if another_try.lower() == "n":
                break


leap_year()