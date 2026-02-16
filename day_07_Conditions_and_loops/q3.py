# Q. Reverse a Number Without Using String

original_number = int(input("Enter a number: "))

number = original_number
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print('Original number : ',original_number)
print('Reversed number : ',reversed_number)