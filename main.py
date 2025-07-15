import os
import time
import platform

char_map = {
    "a": 1, "z": 2, "e": 3, "r": 4, "t": 5,
    "y": 6, "u": 7, "i": 8, "o": 9, "p": 10,
    "q": 11, "s": 12, "d": 13, "f": 14, "g": 15,
    "h": 16, "j": 17, "k": 18, "l": 19, "m": 20,
    "w": 21, "x": 22, "c": 23, "v": 24, "b": 25,
    "n": 26
}

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_password(prompt="Password: "):
    return input(prompt)

def register_user():
    clear_screen()
    print("=== Person 1 Registration ===")
    username = input("Enter your username: ")

    for tries_left in range(3, 0, -1):
        password = get_password("Enter password (no '.' or space allowed): ")
        if "." in password or " " in password:
            print("Error: password cannot contain '.' or space.")
            continue
        password_confirm = get_password("Confirm password: ")
        if password != password_confirm:
            print(f"Passwords do not match. Try again. Attempts left: {tries_left-1}")
            continue
        return username, password
    print("Failed to set a valid password after 3 attempts.")
    exit()

def check_login(expected_username, expected_password):
    clear_screen()
    print("=== Person 2 Login ===")
    username = input("Enter your username: ")
    if username != expected_username:
        print("Unknown username. Access denied.")
        return False
    password = get_password("Enter your password: ")
    if password != expected_password:
        print("Wrong password. Access denied.")
        return False
    return True

def main():
    user1_name, user1_password = register_user()

    clear_screen()
    print(f"Welcome {user1_name}! Please enter your message to encrypt:")
    user_message = input("Message: ")

    converted = []
    for char in user_message:
        if char.lower() in char_map:
            converted.append(str(char_map[char.lower()]))
        else:
            converted.append(char)

    print("\nEncrypted message:", " ".join(converted))
    print("Message stored securely.")

    time.sleep(3)
    clear_screen()

    if not check_login(user1_name, user1_password):
        exit()

    print(f"The message was: {user_message}")

if __name__ == "__main__":
    main()
