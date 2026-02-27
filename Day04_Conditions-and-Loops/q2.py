# Take a number from the user and count:
#  1. How many even digits
#  2. How many odd digits


num = int(input("Enter a number:"))
num = abs(num)

even_digit = 0
odd_digit = 0


if num == 0:
    even_digit = 1
    odd_digit = 0
else:
    even_digit = 0
    odd_digit = 0


# extract even and odd digits
while num !=0:
    digit = num % 10
    if digit % 2 == 0:
        even_digit += 1
    else:
        odd_digit +=1
    num = num // 10

print("Even Digits: ",even_digit)
print("Odd Digits: ",odd_digit)