# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:55:33 2024

@author: Mohit Kumar Pani
"""

import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_lowercase + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        print("Invalid complexity level. Please select from 'low', 'medium', or 'high'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter complexity level (low, medium, high): ").lower()

    password = generate_password(length, complexity)

    if password:
        print("Generated Password:", password)
