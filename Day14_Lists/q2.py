# Q.2 Count Even and Odd Numbers in a List

num_list = []


N_number = int(input('Enter how many number : '))
print("Enter numbers : ")

for i in range(N_number):
    num = int(input())
    num_list.append(num)

count_even = 0
count_odd = 0
for i in num_list:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1


print('Even number : ',count_even)
print('Odd number : ',count_odd)
