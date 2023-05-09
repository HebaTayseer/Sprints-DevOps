# This function takes a string of brackets then determine whether each sequence of brackets balanced or not.
# If a string is balanced it returns YES, otherwise it returns NO.
def is_balanced():

    while True:
        string = input('Enter a string of brackets : ')
        brackets = ['(', ')', '{', '}', '[', ']']
        # Checking that the string contains brackets only.
        if not all(s in brackets for s in string):
            print('Please enter brackets only ! ')
            continue
        else:
            # Checking that the length of the string is even number.
            if int(len(string)) % 2 != 0:
                print('NO')
            else:
                # Splitting the string in to two equal halves.
                first_half = string[:len(string) // 2]
                second_half = string[len(string) // 2:]
                # Reversing the second half.
                r_second_half = second_half[::-1]
                # Checking whether the sequence of the brackets is balanced or not.
                for x, y in zip(first_half, r_second_half):
                    if (x == '(' and y == ')') or (x == '[' and y == ']') or (x == '{' and y == '}'):
                        output = "YES"
                    else:
                        output = "NO"
                        break
                print(output)

        # Asking user if he needs to check another string
        another_try = input("Do you want to check another string ? (y/n) ")
        if another_try.lower() == "n":
            break
        else:
            continue

# Calling the function
is_balanced()
