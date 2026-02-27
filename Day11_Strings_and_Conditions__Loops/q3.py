# Q. Remove Duplicate Characters from a String

text = input("Enter a string: ")

character = ""

for char in text:
    if char not in character:
        character += char

print(character)