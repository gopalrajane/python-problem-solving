1. # Q. Find All Pairs in a List Whose Sum is Equal to K


num_list = []

N = int(input('Enter N number : '))

print('Enter Numbers of list : ')
for i in range(N):
    num = int(input())
    num_list.append(num)

new_list = []
for i in range(len(num_list)):
    last_digit = num_list[-1]
    new_list.append(last_digit)
    num_list = num_list[:-1]

print(new_list)