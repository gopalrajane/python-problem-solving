# Q. Remove Duplicates from a List (Without Using set)

num_list = []


N_number = int(input("Enter number : "))


print('Enter numbers : ')
for i in range(N_number):
    num = int(input())
    num_list.append(num)


new_list = []
for i in num_list:
    if i not in new_list:
        new_list.append(i)


print(new_list)
    