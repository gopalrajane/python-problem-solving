# Q. Count Even and Odd Numbers in a Tuple

num_list = [] # define list

N = int(input('Enter N number : '))  # taking input of n 

for i in range(N):
    num = int(input())
    num_list.append(num)   # # taking input of list number and store in list    num_list.append(num)

num_tuple = tuple(num_list) # convert list into tuple
even_count = 0
odd_count = 0

for i in num_tuple:
    if i % 2 == 0:  # checking number is divisible by 2 for even count
        even_count += 1
    else:            # else the odd_count increased
        odd_count += 1
print('tuple :',num_tuple)
print('Even Number count in tuple :',even_count)
print('Odd Number count in tuple :',odd_count)
