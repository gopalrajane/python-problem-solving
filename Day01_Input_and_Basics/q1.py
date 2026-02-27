# Q. Take two numbers as input from the user and calculate their sum, difference, product, and division.

# Taking input from the user
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# Calculating sum, difference, product and division

sum = num1 + num2
difference = num1 - num2
Product = num1 * num2
if num2 != 0:
    division = num1 / num2

# Displaying the results of the calculations

print("Sum : ", sum)
print("Difference :", difference)
print("Product :", Product)
if num2 != 0:
    print("Division :", division)
