from password import Password

MAX_PASSWORD_LENGTH = 20
MIN_PASSWORD_LENGTH = 8
MIN_CHARACTER = 2
while True:
    try:
        password_length = int(input("Set you password length (%d-%d characters): "
                                    % (MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)))
        characters_left = int(password_length)
        if not MIN_PASSWORD_LENGTH <= password_length <= MAX_PASSWORD_LENGTH:
            print("Incorrect password length. Password must be in range %d - %d characters. Try again!"
                  % (MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH))
            break

        number_of_digits = int(input("Set number of digit in password (min %d - max %d): " %
                                     (MIN_CHARACTER, characters_left - MIN_CHARACTER * 3)))
        if not MIN_CHARACTER <= number_of_digits <= characters_left - MIN_CHARACTER * 3:
            print("Incorrect number of digit.")
            break
        else:
            characters_left -= number_of_digits

        number_of_special_characters = int(input("Set number of special characters in password "
                                                 "(min %d - max %d): "
                                                 % (MIN_CHARACTER, characters_left - MIN_CHARACTER * 2)))
        if not MIN_CHARACTER <= number_of_special_characters <= \
               characters_left - MIN_CHARACTER * 2:
            print("Incorrect number of special characters.")
            break
        else:
            characters_left -= number_of_special_characters

        number_of_uppercase_letters = int(input("Set number of uppercase letters in password "
                                                "(min %d - max %d): "
                                                % (MIN_CHARACTER, characters_left - MIN_CHARACTER)))
        if not 1 <= number_of_uppercase_letters <= characters_left - MIN_CHARACTER:
            print("Incorrect number of uppercase letters.")
            break
        else:
            characters_left -= number_of_uppercase_letters

        number_of_lowercase_letters = characters_left
        print("Number of lowercase letters is: %d" % characters_left)

        print(number_of_digits, number_of_special_characters, number_of_uppercase_letters, number_of_lowercase_letters)

        password = Password(number_of_digits, number_of_special_characters,
                            number_of_uppercase_letters, number_of_lowercase_letters)
        print(password.create_password())

    except ValueError:
        print("This value must be positive integer. Try again!")
