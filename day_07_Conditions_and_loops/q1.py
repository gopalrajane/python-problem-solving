# Q. Check if a Number is an Armstrong Number


number = int(input("Enter a number: "))

num = number
N = number

count = 0
while num != 0:
    count += 1
    num = num // 10

count_number_mul = 0
while N != 0:
    digit = N % 10

    count_number_mul += digit ** count
    N = N // 10

if number == count_number_mul:
    print(f'{number}, is a armstrong number')
else:
    print(f'{number}, is not a armstrong number')


