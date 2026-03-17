# Q. Function to Find Largest Number in a List

def  largest_number(N):

    num_list = []
    print("Enter list number : ")
    for i in range(1,N+1):
        num = int(input())
        num_list.append(num)

    largest_number = num_list[0]
    for i in num_list:
        if i > largest_number:
            largest_number = i
            
    print("largest number :",largest_number)


N = int(input("Enter N :"))
largest_number(N)

    





     
