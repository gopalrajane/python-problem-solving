# Q. Create a Dictionary of Squares


# Define ditionary
Data = {}


# take input of n number
N_number = int(input("Enter N : "))


# loop run the n number and i store in keys of ditionary
#  i * i calculate square and storing in dictionary values
for i in range(1,N_number+1):
    Data[i] = i * i

print(Data)