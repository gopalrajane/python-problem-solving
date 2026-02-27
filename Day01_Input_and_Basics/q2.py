# Q. Take a student’s name and marks of three subjects as input from the user. Calculate and display the total marks and percentage.


# Taking input name and marks from the student
name = input("Enter name of the student: ")
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks if subject 3: "))


# Calculating the Total Marks and Percentages.
total_marks = marks1 + marks2 + marks3
percentages = (total_marks/ 300) * 100

# Displaying the marks and Percentages
print("Name of the Student : ",name)
print("Total Marks :",total_marks)
print("Percentage :",percentages)








