# Q. Find Unique Elements From Two Lists
list_1 = []  # Define the lists
list_2 = []

print('Enter list 1 digits :')
for i in range(5):    # Take input and store in list 1
    num_1 = int(input())
    list_1.append(num_1)

print('Enter list 2 digits :')
for i in range(5):  # Take input and store in list 2
    num_2 = int(input())
    list_2.append(num_2)

set_1 = set(list_1)  # Convert the lists into sets
set_2 = set(list_2)

print(set_1.symmetric_difference(set_2)) # For uniwue value use symmetric.difference() function
