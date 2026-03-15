# List Statistics Function 
# 1. list sum
# 2. average
# 3. maximum
# 4. minimum

numbers = [10,20,30,40,50]

def list_stats(numbers):
    sum_of_list = 0
    max_number = numbers[0]
    min_number = numbers[0]
    for i in numbers:
        sum_of_list += i
        average = sum_of_list / len(numbers)
        
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i
            print(min_number)

    print("Sum =",sum_of_list)
    print("Average =",average)
    print("Max =",max_number)
    print("Min =",min_number)

list_stats(numbers)