# Q. Dictionary Reverse


# Define the Ditionary
Student = {
    'Student_1' : 'Gopal',
    'Student_2' : 'Pravin',
    'Student_3' : 'Karan',
    'Student_4' : 'Arjun',
    'Student_5' : 'Arvind'
}

# Create a New Ditionary to store reverse Ditionary
New_student = {}


# In this line abstract keys and values from Stundet Ditionary using items function.
for keys,values in Student.items():
    New_student[values] = keys  # This Store keys on value place and value on keys place


# Printint the reverse ditionary output
print("Reverse Ditionary : ",New_student)