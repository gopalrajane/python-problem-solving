# Check whether a number is an Armstrong number.


original_number = int(input("Enter a number: "))
num = original_number
num = abs(num)

# step 1. count digits
count = 0
while num != 0:
    count += 1
    num = num // 10


# step 2. checking armstrong number
num = original_number
power_of_total = 0
while num != 0:
    digit = num % 10
    power_of_total += digit ** count
    num = num // 10

# step 3. Compare
if original_number == power_of_total:
    print(f'{original_number}, is a armstrong number.')
else:
    print(f'{original_number}, is not a armstrong number.')
