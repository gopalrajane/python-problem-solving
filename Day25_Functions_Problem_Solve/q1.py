# Number Analyzer Function


def number_analyzer(num):
    if num % 2 == 0:
        print(num,"is a Even Number.")
    else:
        print(num,"is a Odd Number.")
    
    if num > 0:
        print(num,"is Positive.")
    elif num < 0:
        print(num,"is Negative.")
    else:
        print(num,"is Zero.")


num = int(input("Enter Number : "))
number_analyzer(num)


