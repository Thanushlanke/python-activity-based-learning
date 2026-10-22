# Question: Password Policy Validation Engine - Evaluate sample password strings against minimum length requirement.
password = input("Enter your password: ")

if len(password) >= 8:
    print("Password validation successful.")
else:
    print("Password is too short. Must be at least 8 characters.")