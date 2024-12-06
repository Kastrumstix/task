import re


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    def __init__(self, username, password, password_confirm):
        # pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+$'
        self.username = username
        # if re.match(pattern, password):
        self.password = password
        #else:
        #   print("Enter correct password")
        #    exit()


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Change your desteny: \n1 - Enter\n2 - Registration\n"))
        if choice == 1:
            login = input("Enter login: ")
            password = input("Enter password: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Hi {login}")
                else:
                    print("Error password")
            else:
                print("User not found")
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите логин: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Error")
                continue
            database.add_user(user.username, user.password)
