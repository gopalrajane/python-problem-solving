# Q. Count the Frequency of Each Character in a String.

text = input("Enter a strings: ")

dictionary = {}

for char in text:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

    
for char, count in dictionary.items():
    print(char,':',count)


