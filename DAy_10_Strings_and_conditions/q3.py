# Q. Check if Two Strings are Anagrams

text_1 = input("Enter First Strings: ")
text_2 = input("Enter Second Strings: ")

if len(text_1) != len(text_2):
    print('Strings are not Anagrams because of length is not same.')
else:
    is_anagram = True

    for i in text_1:
        if text_1.count(i)  != text_2.count(i):
            is_anagram = False
            break



if is_anagram:
    print(f'Strings  1."{text_1}"  and  2."{text_2}"  are Anagram.')
else:
    print(f'Strings  1."{text_1}" and 2."{text_2}" are not Anagram.')

