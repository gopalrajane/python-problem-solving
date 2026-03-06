# Q. Convert Tuple to List and Remove Duplicates

num_tuple = (1,2,2,3,6,6,9,0,4,4,5)  # tuple of number

num_list = list(num_tuple) # convert list into tuple

new_list = []   # new list for removing duplicates
for i in num_list:
    if i not in new_list: # it checks the num_list number i present in new list if not then storing in new list 
        new_list.append(i) # if not then not storing

print(new_list)
