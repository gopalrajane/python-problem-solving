# Q. Count How Many Values are Greater Than a Given Number

# Define ditioanary
marks = {
    "Rahul":80,
    "Amit":92,
    "Neha":67,
    "Riya":78,
    "Rohan":87,
    "Vikas":72
}

# take input of given number
given_number = int(input('Enter a number : '))

count = 0 # define the count variable to calculate count
for i in marks.values():  # loop abstract the dictionary values 
    if i > given_number:  # checks value greater or not if greater then count increase by 1
        count += 1

# Shows the output
print(count)
