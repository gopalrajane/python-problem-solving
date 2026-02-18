# Q. Check if a String is a Palindrome

string = input("Enter a string: ")

# this isfor comapring with reversed_string .
original_string = string

reversed_string = '' # to storing reversed string.
while len(string) > 0:  # runs until length of string is greater than 0.
    reversed_string = reversed_string + string[-1] # add last leter in variable
    string = string[:-1] # update remaining all letters 

    
if original_string == reversed_string: # comparing original string with reversed string
    print(f' "{original_string}", The string is a palindrome.')
else:
    print(f' "{original_string}", The string is not a palindrome.')

