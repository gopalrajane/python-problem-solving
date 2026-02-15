# Q. Print all Prime Numbers Between Two Numbers


start_num = int(input("Enter a number: "))
end_num = int(input("Enter a number: "))

# if starter number is greater than end number then swap the number
if start_num > end_num:
    start_num, end_num = end_num, start_num


# for store number range value in num
for num in range(start_num,end_num+1):
    if num > 1:        # if number is greater than 1 then the excute beacuase prime number is always greater than 1
        is_prime = True


        for i in range(2,num):
            if num % i == 0: # check numer is divide or not if divide then is_prime = False else  True 
                is_prime = False
                break
            
        if is_prime:
            print(num)