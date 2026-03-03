# Q. Find the First Duplicate Element in a List

num_list = []

N = int(input('Enter N number : '))

print('Enter Numbers of list : ')
for i in range(N):
    num = int(input())
    num_list.append(num)

for i in num_list:
    num_list = num_list[1:]
    for j in num_list:
        if i == j:
            duplicate_number = i
    break


print(f'First duplicate number : {duplicate_number}')