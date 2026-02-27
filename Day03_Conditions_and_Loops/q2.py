# Q. Take a number from the user and count how many digits are present in that number.

num = int(input("Enter a number: "))


# variable to store reverse number.
rev = 0 
while num != 0:
    digit = num % 10 # Extract last digits
    rev = rev * 10 + digit # building the reverse number
    num = num // 10 # remove last digit


print("Reversed Number:",rev)



