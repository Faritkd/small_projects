import random
import string

def generate_password():
    # Define characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    length = int(input("Enter the length of password:"))
    password = ''.join(random.sample(characters, length))
    return password

# Example usage: generate a 16-character password
generated_password = generate_password()
print("Generated password:", generated_password)



# string.ascii_letters includes all uppercase and lowercase letters.
# string.digits includes digits (0-9).
# string.punctuation includes special characters like !@#$%^&*()