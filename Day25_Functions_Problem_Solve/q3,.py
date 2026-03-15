# Password Strength Checker

def check_password(password):

    has_digit = False
    has_upper = False
    has_lower = False

    for char in password:

        if char.isdigit():
            has_digit = True

        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

    if len(password) >= 8 and has_digit and has_upper and has_lower:
        print("Strong Password")
    else:
        print("Weak Password")


check_password("Gopal123")


