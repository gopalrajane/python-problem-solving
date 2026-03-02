# Q. Find the Second Largest Number in a List (Without Using sort or max)

num_list = [3, 4, 5, 7, 8, 6, 9]

largest_number = 0
second_largest = 0

for i in num_list: # this is use for accesing the list
    if i > largest_number: # if i is greater than larget_number = 0 
        second_largest = largest_number # second largest beacomes largest which is 0
        largest_number = i # i beacomes larget number
    if largest_number > i and second_largest < i: 
        second_largest = i


print(f'largest number : {largest_number}')
print(f'Second largest : {second_largest}')


if largest_number > second_largest:
    print(second_largest)

