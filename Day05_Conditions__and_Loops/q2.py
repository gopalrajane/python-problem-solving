# Q. Find the Largest Digit in a Number.

Num = int(input("Enter a number: "))

# If number is negative, convert it to positive
# because digit extraction works the same for positive numbers
Num = abs(Num)

# This variable will store the largest digit found so far
largest = 0

# Loop runs until all digits are removed
while Num != 0:
    
    # Extract the last digit
    digit = Num % 10
    
    # Compare current digit with the stored largest value
    # If current digit is bigger, update largest
    if digit > largest:
        largest = digit
    
    # Remove the last digit from number
    Num = Num // 10

# If the user enters 0, loop will not run
# So we handle that case separately
if largest == 0:
    print("Largest digit:", 0)
else:
    print("Largest digit:", largest)
