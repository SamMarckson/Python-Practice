"""
Title: Land perimeter
Source: https://www.codewars.com/kata/5839c48f0cf94640a20001d3/python
Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands.
 Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a
 perfect 1 x 1 piece of land. Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']
"""


def land_perimeter(arr):

    sumSides = 0

    if len(arr) == 1:
        return (f"Total land perimeter: 4")

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 'X':
                contSides = 4
                if i == 0 and (j > 0 and j < len(arr[i]) - 1):                      #EXTREMIDADE SUPERIOR
                    if arr[i][j+1] == 'X':
                        contSides -= 1
                    if arr[i][j-1] == 'X':
                        contSides -= 1
                    if arr[i+1][j] == 'X':
                        contSides -= 1
                if i == 0 and j == 0:
                    if arr[i][j+1] == 'X':
                        contSides -= 1
                    if arr[i+1][j] == 'X':
                        contSides -= 1
                if i == 0 and j == len(arr[i]) - 1:
                    if arr[i][j-1] == 'X':
                        contSides -= 1
                    if arr[i+1][j] == 'X':
                        contSides -= 1

                if (i == len(arr) - 1) and (j > 0) and (j < len(arr[i]) - 1):            #EXTREMIDADE INFERIOR
                    if arr[i][j+1] == 'X':
                        contSides -= 1
                    if arr[i][j-1] == 'X':
                        contSides -= 1
                    if arr[i-1][j] == 'X':
                        contSides -= 1
                if i == len(arr) - 1 and j == 0:
                    if arr[i][j+1] == 'X':
                        contSides -= 1
                    if arr[i-1][j] == 'X':
                        contSides -= 1
                if i == len(arr) - 1 and j == len(arr[i]) - 1:
                    if arr[i][j-1] == 'X':
                        contSides -= 1
                    if arr[i-1][j] == 'X':
                        contSides -= 1

                if (i > 0 and i < len(arr) - 1) and j == 0:   #MIOLO
                    if arr[i][j+1] == 'X':
                        contSides -= 1
                    if arr[i-1][j] == 'X':
                        contSides -= 1
                    if arr[i+1][j] == 'X':
                        contSides -= 1
                if (i > 0 and i < len(arr) - 1) and j == len(arr[i]) - 1:
                    if arr[i][j-1] == 'X':
                        contSides -= 1
                    if arr[i - 1][j] == 'X':
                        contSides -= 1
                    if arr[i + 1][j] == 'X':
                        contSides -= 1
                if (i > 0 and i < len(arr) - 1) and (j > 0 and j < len(arr[i]) - 1):
                    if arr[i][j+1] == 'X':
                        contSides -= 1
                    if arr[i][j-1] == 'X':
                        contSides -= 1
                    if arr[i-1][j] == 'X':
                        contSides -= 1
                    if arr[i+1][j] == 'X':
                        contSides -= 1

                sumSides += contSides
    return (f"Total land perimeter: {sumSides}")


#MAIN
print(land_perimeter(["X"]))


