# Q. Check if a String Contains Only Digits

text = input('Enter a String : ')

digit = set('1234567890')

is_digit = True

for i in text:
    if i not in digit:
        is_digit = False
        break


if is_digit:
    print('Strings Contains Only Digits.')
else:
    print('Strings does not Contains Only Digits.')