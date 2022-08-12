import random
import string


class Password:

    def __init__(self, digits, special_characters, uppercase, lowercase):
        self.digits = digits
        self.special_characters = special_characters
        self.uppercase = uppercase
        self.lowercase = lowercase

    def create_password(self):
        password = [random.choice(string.digits) for _ in range(self.digits)] + \
                   [random.choice(string.punctuation) for _ in range(self.special_characters)] + \
                   [random.choice(string.ascii_uppercase) for _ in range(self.uppercase)] + \
                   [random.choice(string.ascii_lowercase) for _ in range(self.lowercase)]
        random.shuffle(password)
        return "".join(password)
