# Q 1. Find the Largest Number in a List

num_list = []


N_number = int(input("Enter a number : "))

print('Enter numbers : ')
for i in range(N_number):
    num = int(input())
    num_list.append(num)


largest_number = num_list(0)
for list_num in num_list:
    if list_num > largest_number:
        largest_number = list_num


print(f'Largest number is : {largest_number}')



