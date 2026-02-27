# Q. Find the First Non-Repeating Character in a String.

text = input("Enter a String: ")

dictonary = {}

for char in text:
    if char in dictonary:
        dictonary[char] += 1
    else:
        dictonary[char] = 1

#   Option 1
for char,count in dictonary.items():
    if count == 1:
        print('First Non_repeating character : ',char)
        break


#   Option 2
for char in text:
    if dictonary[char] == 1:
        print('First Non_repeating character : ',char)
        break
