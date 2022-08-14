from password import Password

MAX_PASSWORD_LENGTH = 30  # max password length
MIN_CHARACTER = 1  # min amount of each type of char
MIN_PASSWORD_LENGTH = 4 * MIN_CHARACTER  # min password length at least 4 x each type of characters


def get_from_user(char_left, char_type, number_choice=1):
    """
     Function responsible for getting value of number of digits, special characters, uppercase letter form the user,
     validation correct type of variable and return the characters left and user choice

    :param char_left: possible left character to use
    :param char_type: type of character getting from user
    :param number_choice: variable using to safe minimum character left to each variable
    :return: number of character left, number of each character
    """
    while True:
        try:
            user_choice = int(input("Set number of %s in password (min %d - max %d): " %
                                    (char_type, MIN_CHARACTER, char_left - MIN_CHARACTER * number_choice)))
            if not MIN_CHARACTER <= user_choice <= char_left - MIN_CHARACTER * number_choice:
                print("Incorrect number of %s." % char_type)
                continue
            else:
                char_left -= user_choice
            return char_left, user_choice
        except ValueError:
            print("This value must be positive integer. Try again!")


while True:
    """
    Main program loop, get password length from user and check input correctness
    """
    try:
        password_length = int(input("Set you password length (%d-%d characters): "
                                    % (MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)))
        characters_left = int(password_length)
        if not MIN_PASSWORD_LENGTH <= password_length <= MAX_PASSWORD_LENGTH:
            print("Incorrect password length. Password must be in range %d - %d characters. Try again!"
                  % (MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH))
            continue
        characters_left, number_of_digits = get_from_user(characters_left, "digit", 3)
        characters_left, number_of_special_char = get_from_user(characters_left, "special characters", 2)
        characters_left, number_of_uppercase = get_from_user(characters_left, "special characters")
        number_of_lowercase = characters_left
        print("Number of digits: %d" % number_of_digits)
        print("Number of special characters: %d" % number_of_special_char)
        print("Number of uppercase letters: %d" % number_of_uppercase)
        print("Number of lowercase letters: %d" % characters_left)
        password = Password(number_of_digits, number_of_special_char,
                            number_of_uppercase, number_of_lowercase)
        print(password.create_password())

    except ValueError:
        print("This value must be positive integer. Try again!")
