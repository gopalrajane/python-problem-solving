# Q. Find the Longest Word in a Sentence

sentence = input("Enter a Sentence : ")

current_word = ""
longest_word = ""

for char in sentence:
    if char != " ":
        current_word += char
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""
           
print(longest_word)
if len(current_word) > len(longest_word):
    longest_word = current_word 

print('Longest Word : ',longest_word)
