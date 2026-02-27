# Q. Check if a Number is a Strong Number

N = int(input("Enter a number: "))

# to store value for checking factorial if not store then comparing value = 0 because when while loops runs the values becomes zero
num = N

sum_fact = 0
while num != 0:
    digit = num % 10
    
    fact = 1

    # Calculating Factorial of1 to digit +1 for the last digit is not count by range function
    for i in range(1,digit+1):
        fact *= i  
    sum_fact += fact  # This variable for storing sum of all digits factorial 
    num = num // 10

# checking original number is equal to sum of all digits factorial
if N == sum_fact:
    print(f'{N},is a strong number')
else:
    print(f'{N},is not a strong number')

       
