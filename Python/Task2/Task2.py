def leap-year():
        year = input("Enter the year you want to check: ")
    while True:
        try:
            # reads the index where we want to insert a new character and converts it into number.
            year = int(year)
        # validate that the user entered an integer
        except ValueError:
            print('Please enter a valid integer!')
        else:
            break
leap-year()