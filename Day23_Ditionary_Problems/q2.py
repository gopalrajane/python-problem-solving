# Q. Find the Sum of All Values in a Dictionary


# Define ditionary
data = {
    'A':10,
    'B':20,
    'C':30,
    'D':40,
    'E':50,
    'F':60
}

Sum_of_dta_values = 0  # This variable define for storing the sum of values
for i in data.values():  # loop access the values of ditionary 
    Sum_of_dta_values += i # add in sum varibale


# shows output
print('Sum of all Ditionary values : ',Sum_of_dta_values)

# other option
sum(data.values())