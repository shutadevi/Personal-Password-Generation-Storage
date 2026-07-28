import random
import secrets

print("Welcome to the Password Generator!")

#Input parameters for password generation
password_length = int(input("Enter password length: "))
add_characters = input("Add any characters you would like to specifically include in the pool of characters: ")
restricted_characters = input("Enter any characters you would like to restrict from the pool of characters: ")

#Character pool
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+" + add_characters

# Remove restricted characters from the pool
for char in restricted_characters:
    characters = characters.replace(char, '')

#Generation of random password
password = ''
for i in range(password_length):
    password += secrets.choice(characters)

print("Generated Password:", password)
