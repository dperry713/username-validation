class UsernameError(Exception):
    def __init__(self, message="Invalid username"):
        super().__init__(message)
def check_username(username):
    MIN_USERNAME_LENGTH = 6

    if len(username) < MIN_USERNAME_LENGTH:
        raise UsernameError("Username must be at least 6 characters long")

    # Additional validation logic can be added here if needed
    # For example, checking for special characters, whitespace, etc.

    return True  # Username is valid

def main():
    try:
        user_input = input("Enter a username: ")
        check_username(user_input)
        print("Username is valid. Welcome!")
    except UsernameError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
