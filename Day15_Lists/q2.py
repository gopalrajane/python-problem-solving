# Q. Move All Zeros to the End of the List

num_list = []

N = int(input("Enter N number : "))

for i in range(N):
    num = int(input())
    num_list.append(num)

count = 0
non_zero_list = []
for i in num_list:
    if i != 0:
        non_zero_list.append(i)
    else:
        count += 1

zero = 0
for i in range(count):
    non_zero_list.append(zero)

print(non_zero_list)
