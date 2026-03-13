# Q. Create Dictionary From Two Lists (Without zip())

Data = {}  # Define dictionary

keys = ['A','B','C','D','E']  # list1 1
values = [10,20,30,40,50]    # list 2


# this loop range in start_value minimum length of keys and end_value is length pf values
for i in range(min(len(keys), len(values))):
    Data[keys[i]] = values[i]  # this store keys and values in dictionary


# Print Output
print(Data)