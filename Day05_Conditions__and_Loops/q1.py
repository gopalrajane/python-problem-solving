# Q. Check if a Number is a Perfect Number.


# Take a number input
Num  = int(input("Enter a Number: "))

Num_sum = 0

if Num <= 0:  # check number is greater or smaller
    print("Perfect numbers must be positive.")
else: 
    for r in range(1, Num):  # Divide the number and add in variable
        if Num % r == 0:
            Num_sum += r


    if Num == Num_sum: # check number equal or not
        print(f'{Num},is a perfect number.')
    else:
        print(f'{Num},is not a perfect number.')



 