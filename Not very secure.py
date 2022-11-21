"""
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None,
so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""


def alphanumeric(password):
    cont = 0
    for i in range(0, len(password)):
        if ord(password[i]) >= 65 and ord(password[i]) <= 90 or ord(password[i]) >= 97 and ord(password[i]) <= 122 or ord(password[i]) >= 48 and ord(password[i]) <= 57:
            cont += 1

    if cont == len(password) and len(password) > 0:
        return True
    else:
        return False


#MAIN
print(alphanumeric(""))