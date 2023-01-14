"""
Title: Rot13
Source: https://www.codewars.com/kata/530e15517bc88ac656000716/python
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
 ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
 characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
 should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
"""


def rot13(message):
    message = list(message)
    for i in range(0, len(message)):
        if (ord(message[i]) >= 65 and ord(message[i]) <= 90) or (ord(message[i]) >= 97 and ord(message[i]) <= 122):
            if (ord(message[i]) <= 77) or ord(message[i]) >= 97 and ord(message[i]) <= 109:
                message[i] = chr(ord(message[i]) + 13)
            elif (ord(message[i]) > 77 and ord(message[i]) <= 90) or (ord(message[i]) > 109 and ord(message[i]) <= 122):
                message[i] = chr(ord(message[i]) - 13)
    return ''.join(message)


#MAIN
print(rot13('aA bB zZ 1234 *!?%'))