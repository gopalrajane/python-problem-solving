# Q. Rotate a List to the Right by K Steps (Without Using Built-in Functions)

# K means how much times abstract the last digit of list and add it to starting position
Num_list = []

N = int(input('Enter N number : '))  # inputs the N number

print("Enter list numbers : ") 
for i in range(N): # loop run until take input to N number
    Num = int(input())
    Num_list.append(Num) # this lines add the all inputs digit in list 

rotation_k = int(input("How many times you want to rotate : ")) # this input for how much times we want 
#                                                               # to add last digit on first position

for i in range(rotation_k):  # loop run until the rotation K 
    for i in Num_list:
        last_digit = Num_list[-1] # abstract the last digit
        Num_list = Num_list[:-1]   # update list to last digit and remove the last digit
        Num_list.insert(0,last_digit)  # this lines add the last digit on first position
        break
        

print(Num_list)