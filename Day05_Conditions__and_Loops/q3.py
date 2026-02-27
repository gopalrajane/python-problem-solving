# Q. Print All Prime Numbers from 1 to N.

Num = int(input("Enter a number: "))

# Loop through every number from 1 to Num
# We will check each number individually
for N in range(1, Num + 1):

    # Prime numbers are always greater than 1
    if N > 1:

        # Assume the current number is prime
        # If we find any divisor, we will change this to False
        is_prime = True

        # Try dividing N by all numbers from 2 to N-1
        # If any number divides it completely,
        # then N is not a prime number
        for i in range(2, N):
            if N % i == 0:
                is_prime = False  # divisor found
                break             # stop checking further

        # If no divisor was found after full checking,
        # then the number is prime
        if is_prime:
            print(N)

        


            




