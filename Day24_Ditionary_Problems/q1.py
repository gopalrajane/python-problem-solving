# Q. Find All Keys with a Specific Value


# Define ditionary 
data = {
    'A':10,
    'B':20,
    'C':10,
    'D':30,
    'E':20,
    'F':30
}

# take input of search value
search_value = int(input("Enter a value : "))
value_found = False

for keys,values in data.items(): # loop abstract the keys and values of Ditionary
    if values == search_value: # this compare the search value with dictionary values
        print(keys) # print the keys
        value_found = True
    
# this print if value is not found
if not value_found:
    print('Value not found.')
        
        

    
