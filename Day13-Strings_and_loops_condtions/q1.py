# Q. Check if Two Strings are Exactly Same Without Using

text_1 = input("Enter First String : ")
text_2 = input("Enter Second String : ")


if len(text_1) != len(text_2):
    print("Strings are not same exactly.")
else:
    is_same_str = True

    for i in range(len(text_1)):
        if text_1[i] != text_2[i]:
            is_same_str = False
            break

    
    if is_same_str:
        print("Strings are exactly same.")
    else:
        print("Strings are exactly not same.")



