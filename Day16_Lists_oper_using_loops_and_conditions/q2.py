# Q . Check if a List is Palindrome

num_List = [1,2,3,4,5,4,3,2,1]

last_digit = 0           # This is use for abstract the last digit
for i in num_List:
    last_digit = num_List[-1] # last_digit of num_list add in last_digit variable.

    if i == last_digit: # check the last digit and first are similar are not
        palim_drome = True # if same palimdrome becomes true
    else:                 # else false
        palim_drome = False
        break             # break the condtions here beacause we find the palimdrone is not
    num_List = num_List[:-1]  # updating the list remove last digit 

    

if (palim_drome):
    print('List are Palimdrome.')
else:
    print('Lists are not Palimdrome.')
