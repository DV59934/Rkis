class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

    def __str__(self):
        return f"User(Login: {self.Login}, Password: {self.Password})"

users = [
    User("admin", "admin123"),
    User("qwerty", "qwerty123"),
    User("asdfg", "asdfg123"),
    User("zxc", "zxc123"),
    User("lkjh", "lkjh788")
]

search_login = "zxc"
search_password = "zxc123"

found_user = None
for user in users:
    if user.Login == search_login and user.Password == search_password:
        found_user = user
        break

if found_user:
    print(f"Найден пользователь: {found_user}")
else:
    print(f"Пользователь с логином '{search_login}' и паролем '{search_password}' не найден.")