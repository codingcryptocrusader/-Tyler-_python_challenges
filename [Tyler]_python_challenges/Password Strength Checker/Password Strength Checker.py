import string

def is_strong_password(password: str) -> bool:
    """Check if the password meets strength criteria."""
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    has_space = any(char.isspace() for char in password)

    return all([has_upper, has_lower, has_digit, has_symbol]) and not has_space


def main():
    password = input("Enter a password to check: ").strip()
    if is_strong_password(password):
        print("Strong password!")
    else:
        print("Weak password. Try adding uppercase, lowercase, digits, and symbols.")

if __name__ == "__main__":
    main()
