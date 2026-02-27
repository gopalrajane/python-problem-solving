# Q. Take an integer input from the user and calculate the sum of its digits.



num = int(input("Enter a number: "))

num = abs(num) # handle negative numbers
digit = 0
digit_sum = 0 # Accumulator

while num!= 0:
    digit = num % 10 # extract the digit
    digit_sum = digit_sum + digit # add all digits to digit_sum
    num = num // 10 # remove last digit

print("Addition of digits:",digit_sum)