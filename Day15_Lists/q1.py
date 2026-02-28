# Q. Find the Missing Number in a List

num_list = []


N = int(input("Enter numbers: "))
print('Enter list numbers : ')

for i in range(N):
    num = int(input())
    num_list.append(num)

largest_number = 0
for i in num_list:
    if i > largest_number:
        largest_number = i
    
for i in range(1,largest_number+1):
    if i not in num_list:
        print('Missing Number :',i)





        

    
        