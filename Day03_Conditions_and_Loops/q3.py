# Q. Take a number from the user and check whether it is a palindrome number.

N = int(input("Enter a number: "))

# variable to store number value for operation
num = N

# variable to store reverse number.
rev = 0 
while num != 0:
    digit = num % 10 # Extract last digits
    rev = rev * 10 + digit # building the reverse number
    num = num // 10 # remove last digit


if N == rev: # checking number palindrome or not
    print(f"{N}, is a palindrome.")
else:
    print(f"{N}, is not a palindrome.")