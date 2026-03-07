# Q. Remove Duplicates from a List Using Set

list_1 = [1,2,3,4,5]  # Define the list1 & list2
list_2 = [3,4,5,6,7]

set_1 = set(list_1) # Convert the list into tuple using set()
set_2 = set(list_2)

duplicate = set_1.intersection(set_2) # store the duplicate values of tuple variable

print(duplicate)  # print dupliacte values

