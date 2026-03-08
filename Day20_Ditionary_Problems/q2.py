# Q. Find the Key with Maximum Value

# DEfine Product
Product = {}


# Taking Output of keys
Product_1 = int(input('Enter Product 1 Values : '))
Product_2 = int(input('Enter Product 2 Values : '))
Product_3 = int(input('Enter Product 3 Values : '))

# storing Keys and keys values in dictionary using update function
Product.update({'Product_1':Product_1})
Product.update({'Product_2':Product_2})
Product.update({'Product_3':Product_3})

Maximum_value = 0
Maximum_key = ''

# this function takes the key and value of product items 
for key,value in Product.items(): # And check the max values of product
    if value > Maximum_value:  
        Maximum_value = value # It store max value
        Maximum_key = key # it store max key 



# Print the Output
print("Product with maximum value:", Maximum_key)
print("Maximum value:", Maximum_value)
