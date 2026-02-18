# Q. Check if a Number is a Happy Number


num = int(input("Enter a number: "))
N = num # store the number for lastly printing

# looos runs when number != 1 and != 4 beacause the 
# every happpy number eventually becomes 4 and happy hunber is also 1.
while num != 1 and num != 4:
    
    square_num = 0 
    while num != 0: # loops runs until the num is not becomes 0.
        digit = num % 10 # this is for extracting digit from number
        square_num += digit ** 2 # this calculate the square or number
        num = num // 10  # delete the last extracted number

    num = square_num # update some of current numbers

print(num)

# checking number is == 1 for happy number.
if num == 1:
    print(f'{N},is a happy number.')
else:
    print(f'{N},is not a happy number.')



