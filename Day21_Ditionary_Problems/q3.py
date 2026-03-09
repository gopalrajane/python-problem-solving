# Print Even Values with keys form Ditionary.


# Define the Ditionary.
Data = {
    'Number_1' : 17,
    'Number_2' : 72,
    'Number_3' : 55,
    'Number_4' : 22,
    'Number_5' : 67,
    'Number_6' : 90
}


print('Positive values keys.')
for keys, values in Data.items(): # keys and values extracting the items from dictionary using items function.
    if values % 2 == 0:  # It check values are divisible or not 
        print(f'{keys} : {values}') # If divisible then Print the keys with even value.
    