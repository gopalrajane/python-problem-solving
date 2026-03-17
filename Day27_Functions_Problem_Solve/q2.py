# Q. Function to Check Palindrome String


def checker_palimdrome(String_str):
    original_string = String_str
    new_str = ""

    for i in String_str:
        new_str += String_str[-1]
        String_str = String_str[:-1]

    if original_string == new_str:
        print(f'{original_string}, is Palimdrome.')
    else:
        print(f'{original_string}, is not a palimdrome.')




String_str = input("Enter a String : ")
checker_palimdrome(String_str)