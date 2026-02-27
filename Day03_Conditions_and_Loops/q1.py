# Q. Take an integer N as input from the user and calculate the sum of all even numbers from 1 to N.


N = int(input("Enter a number: "))

# variable for storing total numbers.
total = 0
for n in range(1, N+1):   # for loop storing N numbers in n.
    if n % 2 == 0:    # Checking the numbers Even or odd.    n%2 != 0  -> for odd numbers.
        total = total + n   # add in a variable all evem number sum 1 to N.

print("Sum Of All Even Numbers: ",total)