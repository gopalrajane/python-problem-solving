# Q. Count Frequency of Elements in a List

numbers = [1,2,2,3,3,3,4]

freq = {}

for i in numbers:
    
    if i in freq:
        freq[i] += 1
        
    else:
        freq[i] = 1


print(freq)
