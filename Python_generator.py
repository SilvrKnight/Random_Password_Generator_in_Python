import random
import string

def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_digits=True, include_punctuation=True):
    """Generate a random password."""
    try:
        # Create a list of character sets based on user preferences
        character_sets = []
        if include_lowercase:
            character_sets.append(string.ascii_lowercase)
        if include_uppercase:
            character_sets.append(string.ascii_uppercase)
        if include_digits:
            character_sets.append(string.digits)
        if include_punctuation:
            character_sets.append(string.punctuation)

        if not character_sets:
            raise ValueError("At least one character set must be selected.")

        # Generate the password by randomly choosing characters from the selected sets
        password = ''.join(random.choice(random.choice(character_sets)) for _ in range(length))
        return password
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    # Get user input for password generation options
    length = int(input("Enter the desired length of the password: "))
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_punctuation = input("Include punctuation marks? (y/n): ").lower() == "y"

    # Get the number of passwords to generate
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate the passwords
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_punctuation)
        if password:
            passwords.append(password)

    # Print the generated passwords
    if passwords:
        print("Generated passwords:")
        for password in passwords:
            print(password)
    else:
        print("Failed to generate any passwords.")

if __name__ == "__main__":
    main()
