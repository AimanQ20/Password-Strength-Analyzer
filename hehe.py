def check_password_strength(password):
    # Check if password length is less than 8 characters
    if len(password) < 8:
        return "Weak (Too short!)"
    
    # Check if password is the common "password"
    elif password.lower() == "password":
        return "Weak (Common password!)"
    
    # Read the file containing common passwords and check if the password is one of them
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.read().splitlines()
        
    if password in common_passwords:
        return "Weak (Common password found in the list!)"
    
    # If password passes all checks, it's considered strong
    return "Strong!"

# Get password input from user
user_pass = input("Enter a password: ")

# Output the password strength
print(check_password_strength(user_pass))

import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

print(f"MD5 Hash: {hash_password('test123')}")