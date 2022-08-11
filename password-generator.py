while True:
    try:
        password_length = int(input("Set you password length (6-20 characters): "))
        characters_left = int(password_length)
        if not 6 <= password_length <= 20:
            print("Incorrect password length. Password must be in range 6 - 20 characters. Try again!")
            break

        number_of_digits = int(input("Set number of digit in password (min 1 - max %d): " % (characters_left - 3)))
        if not 1 <= number_of_digits <= characters_left - 3:
            print("Incorrect number of digit.")
            break
        else:
            characters_left -= number_of_digits

        number_of_special_characters = int(input("Set number of special characters in password "
                                                 "(min 1 - max %d): " % (characters_left - 2)))
        if not 1 <= number_of_special_characters <= characters_left - 2:
            print("Incorrect number of special characters.")
            break
        else:
            characters_left -= number_of_digits

        number_of_uppercase_letters = int(input("Set number of uppercase letters in password "
                                                "(min 1 - max %d): " % (characters_left - 1)))
        if not 1 <= number_of_uppercase_letters <= characters_left - 1:
            print("Incorrect number of uppercase letters.")
            break
        else:
            characters_left -= number_of_digits

        number_of_lowercase_letters = characters_left
        print("Number of lowercase letters is: %d" % characters_left)

        print(number_of_digits,number_of_special_characters,number_of_uppercase_letters, number_of_lowercase_letters)

    except ValueError:
        print("This value must be positive integer. Try again!")
