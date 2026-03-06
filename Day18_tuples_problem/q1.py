# Q. Find the Largest Element in a Tuple

num_list = [] # Define list for storing values

N = int(input("Enter N number :  ")) # N numbers

for i in range(N):
    num = int(input())
    num_list.append(num) # Taking input and storing in list 

num_tuple = tuple(num_list) # convert list into tuple

Largest_number = num_tuple[0]
for i in num_tuple:  
    if i > Largest_number:  # Checking Largest_number
        Largest_number = i

print('tuple :',num_tuple)
print('Largest Element in a Tuple : ',Largest_number)
