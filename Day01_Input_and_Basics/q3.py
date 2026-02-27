# Q. Take the salary as input from the user and calculate the net salary based on the following tax rules.


# Taking Salary input from user

original_salary = int(input("Enter your salary : "))
print("Original Salary :",original_salary)

if original_salary <= 20000:

    # Tax_rate 0% less than 20 thousand salary
    print("Tax(0%) Ammount : 00.00")
    print("Net Salary :",original_salary)
elif original_salary > 20000 and original_salary <= 50000:

    # Tax_rate 10% for salary is greater than 20 thousand and less than 50 thousand
    tax_rate = (original_salary/100) * 10
    print("Tax(10%) Ammount :",tax_rate)
    net_salary = original_salary - tax_rate
    print("Net Salary : ",net_salary)
elif original_salary > 50000:

    # Tax_rate 20 % for salary is greater than 50 thousad
    tax_rate2 = (original_salary/100) * 20
    print("Tax(20%) Ammount :",tax_rate2)
    net_salary2 = original_salary - tax_rate2
    print("Net Salary : ",net_salary2)
else:
    print("error! Enter right input...")





