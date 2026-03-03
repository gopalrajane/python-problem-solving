# Q. Find All Pairs in a List Whose Sum is Equal to K

num_list = []

N = int(input('Enter N number : '))

print('Enter Numbers of list : ')
for i in range(N):
    num = int(input())
    num_list.append(num)

K = int(input("Enter K : "))

for i in num_list:
    for j in num_list:
        if i + j == K:
            print(f'({i},{j})')
        break


