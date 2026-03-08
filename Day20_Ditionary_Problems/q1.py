# Q> Store Student Marks and Find Average

# Define the dictionary 
Student_marks = {}


# Taking input of Subjects
Phy = int(input("Enter your Physics marks: "))
chem = int(input("Enter your Chemistry marks: "))
math = int(input("Enter your Math marks: "))

# Storing the input in dictionary with keys name
Student_marks.update({'Physics':Phy})
Student_marks.update({'Chemistry':chem})
Student_marks.update({'Math':math})

total = 0

# Calculating the total
for marks in Student_marks.values:
    total += marks


# calculating the average
average = total / len(Student_marks)

# Printing the Output
print('Average Marks :',average)
