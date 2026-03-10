# Q. Merge Two Dictionaries

# Define 1st Ditionary
dict1 = {
    'A' : 10,
    'B' : 20,
    'C' : 30,
    'D' : 40
}

# Define 2nd Ditionary
dict2 = {
    'Student_1' : 'Gopal',
    'Student_2' : 'Pravin',
    'Student_3' : 'Karan'
}

# Printing 1st and 2nd Ditionary Output
print('Ditionary 1 :',dict1)
print('Ditionary 2 :',dict2)

# From update method and or update 2nd Ditionary in 1st Ditionary
dict1.update(dict2)

# Printing tht Output
print('Merged Ditionary 1 & 2 :',dict1)


# 2nd option / 2nd type ---------------------------------------------
merged = {**dict1, **dict2}

print('Merged Ditionary :',merged)

