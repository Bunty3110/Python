import re

def is_valid_username(u):
    return bool(re.fullmatch(r"[A-Za-z0-9@.]+", u))

def is_valid_password(p):
    return bool(re.fullmatch(r"(?=.{5,}$)[A-Za-z0-9@.]*\d", p))

if __name__ == "__main__":
    username = input().strip()
    password = input().strip()
    print("username valid" if is_valid_username(username) else "username invalid")
    print("password valid" if is_valid_password(password) else "password invalid")
