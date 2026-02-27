# Q. Count Vowels in a String


# First Code
string = input("Enter a string: ")

count = 0
for i in string:
    # checking all the vowels values 
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count += 1 # count + 1 if vowels present in string

print(count)


# Second Code

string = input("Enter a string: ")
# store th all vowels values in vowels variable for counting vowels.
vowels = set('aeiouAEIOU')

count = 0
for i in string: # loops runs until last letter of string
    if i in vowels: # check the i is present or not present in vowels set
        count += 1 # count + 1 if vowels present in string

print(f'Total vowels in string, "{string}" : {count}')