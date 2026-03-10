# Q. Word Frequency Counter

# Take input sentence
sentence = input("Enter sentence: ")

# This split each word in separate
words = sentence.split()

# Define the Ditionary for counting frequency
frequency = {}


for word in words: # take a single word from words
    
    if word in frequency:  # it checks word is present or not in ditionary
        frequency[word] += 1 #  add in dict
        
    else:
        frequency[word] = 1

# Print Output
print(frequency)




     