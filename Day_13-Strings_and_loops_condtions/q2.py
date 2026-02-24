# Q. Count Words in a Sentence (Without Using split())

sentence = input("Sentence: ")


count = 0
for i in sentence:
    if i == ' ':
        count += 1

total_words = count + 1
print("Total words in Sentence : ",total_words)