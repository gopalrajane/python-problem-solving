# Q. Check if a Number is a Palindrome

original_number = int(input('Enter a number: '))
number = original_number

reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit 
    number = number // 10

print(reversed_number)

if original_number == reversed_number:
    print(f'{original_number}, is a Palimdrome.')
else:
    print(f'{original_number}, is not a Palimdrome.')
    
