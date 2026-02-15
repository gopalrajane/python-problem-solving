# Q. Find the Second Largest Digit in a Number

num = int(input("Enter a number: "))

largest_num = 0    # variable to store largest number
second_largest = 0    # variable to store second largest

while num != 0:
    digit = num % 10  # extracting digit to check largest number
    if digit > largest_num: # this condition is for checking largest number
        largest_num = digit   
    if digit < largest_num and second_largest < digit: # this condition is for checking second largest
        second_largest = digit
    num = num // 10


if largest_num > second_largest:
    print(f'Second largest number is {second_largest}')


#  improve code 

num = int(input("Enter a number: "))

largest = -1
second_largest = -1

while num != 0:
    digit = num % 10

    # If new digit is bigger than largest
    if digit > largest:
        second_largest = largest   # old largest becomes second
        largest = digit

    # If digit is smaller than largest but bigger than second
    elif digit > second_largest and digit != largest:
        second_largest = digit

    num = num // 10

if second_largest == -1:
    print("No second largest digit")
else:
    print("Second largest digit is", second_largest)
