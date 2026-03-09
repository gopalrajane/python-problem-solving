# Q. Find the largest values key


#  Define the ditionary.
marks = {
    "Rahul": 80,
    "Amit": 92,
    "Neha": 67,
    "Riya": 78
}


Largest_value = 0  # this variable store largest value
Largest_value_key = '' # This variable for storing largest values key

for keys,values in marks.items(): # keys and values extracting the items from dictionary using items function.
    if values > Largest_value: # this check the largest value or greater value
        Largest_value = values  
        Largest_value_key = keys
        
        
# Print the output
print(f'Largest Value Key , {Largest_value_key} : {Largest_value}')

    

