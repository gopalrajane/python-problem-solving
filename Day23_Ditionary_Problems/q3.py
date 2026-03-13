# Q. Check if a Key Exists in Dictionary

# Define the Ditionary
student = {
    'name':'Gopal',
    'age':19,
    'course':'IT',
    'div':'E',
    'roll_no':26
}

# Take input the search key.
search_key = input("Enter key : ")
key_exit = False


# this access all keys and compare search key with dictionary keys
for i in student.keys():
    if search_key == i:
        key_exit = True


# if this true then exists either not exists.
if key_exit:
    print('key exists in ditionary.')
else:
    print('key not exists in ditionary.')


# another method   direct search in ditionary
if search_key in student:
    print("Key exists")
else:
    print("Key not exists")