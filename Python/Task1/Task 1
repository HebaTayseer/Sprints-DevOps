# This function reads a string, changes the character at a given index and then prints the modified string.
def mutate_string():
    # reads the string we need to modify.
    string = input("Enter the string: ")
    while True:
        try:
            # reads the index where we want to insert a new character and converts it into number.
            index = int(input("Enter the index to insert the character at: "))
        # validate that the user entered an integer
        except ValueError:
            print('Please enter a valid integer!')
        else:
            break
    # reads the character we want to insert.
    character = input("Enter the character you want to insert: ")
    # slices the string and inserts the character at the given index.
    string = string[:index] + character + string[index:]
    # prints the modified string.
    print(string)

# calls the function
mutate_string()
