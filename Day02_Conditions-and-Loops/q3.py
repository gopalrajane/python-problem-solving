# Q. Take a number from the user and check whether it is a prime number.


# Taking input from user 
number = int(input("Enter a number: "))


# Checking number is 1 or less than 1
if number <= 1:
    print("Not a prime number")
else:
    is_prime = True

# checking number is prime number.
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")







