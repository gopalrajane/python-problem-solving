# Q. Find All Divisors of a Number Efficiently

num = int(input("Enter a number: "))


print(f'Divisors of number, {num} :')
for i in range(1,num+1):
    if num % i == 0:
        print(i)



    
import math

num = int(input("Enter a number: "))

print(f"Divisors of {num}:")

for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        print(i)
        if i != num // i:
            print(num // i)
