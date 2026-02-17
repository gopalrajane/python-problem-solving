# Q. Find the Largest Prime Factor of a Number

# num = int(input("Enter a number: "))

# print('duv',num%3)
# for i in range(2,4):
#     while num != 0:
#         if num // 2:
#             div = num // 2
#         else:
#             div = num // 3
#             print(2)
#         num = div

num = int(input("Enter a number: "))

largest = None

# Step 1: Remove all factors of 2
while num % 2 == 0:
    largest = 2
    num = num // 2

# Step 2: Check odd numbers from 3 onward
i = 3
while i * i <= num:
    while num % i == 0:
        largest = i
        num = num // i
    i += 2

# Step 3: If anything remains, it is prime
if num > 2:
    largest = num

print("Largest Prime Factor:", largest)
