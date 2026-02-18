# Q. Reverse a String


string = input("Enter a string:  ")

# This is use for storing the reverse value of string.
rev_string = ""

# the loops until the len of string is > 0
while len(string) >  0:
    # Add reverse character into string
    rev_string = rev_string + string[-1]
    string = string[:-1]


print('Reversed string : ',rev_string)
    