import random

print("Welcome to the Password Generator!")

password_length = int(input("Enter password length: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"

password = ''
for i in range(password_length):
    password += random.choice(characters)

print("Generated Password:", password)
