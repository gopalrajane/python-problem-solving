# Q. Find the Most Frequent Element in a List

num_list = []


N = int(input("Enter numbers: "))
print('Enter list numbers : ')


for i in range(N):
    num = int(input())
    num_list.append(num)

max_count = 0
Most_frequent = None
for num in num_list:
    count = 0
    for i in num_list:
        if num == i:
            count += 1
    
    if count > max_count:
        max_count = count
        Most_frequent = num

        
print('Most frequent : ',Most_frequent)
    


