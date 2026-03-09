# Q. Remove Duplicate values with keys

# Define the Ditionary.
Data = {
    'A' : 23,
    'B' : 23,
    'C' : 34,
    'D' : 45,
    'F' : 45,
}

# Creats the new Ditionary for storing non duplicate values
New_data = {}

for keys, values in Data.items():   # keys and values extracting the items from dictionary using items function.
    if values not in New_data.values(): # check the values are present in new dict 
        New_data[keys] = values # if not then store 

# Print the output
print('Data Without Duplicate.')
print(New_data)