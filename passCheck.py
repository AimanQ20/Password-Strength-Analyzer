def check_password_strength(password):
    if len(password) < 8:
        return "Weak (Too short!)"
    
    elif password.lower() == "password":
        return "Weak (Common password!)"
    
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.read().splitlines()
        
    if password in common_passwords:
        return "Weak (Common password found in the list!)"
    
    return "Strong!"

user_pass = input("Enter a password: ")

print(check_password_strength(user_pass))

import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

print(f"MD5 Hash: {hash_password('test123')}")