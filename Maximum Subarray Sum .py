"""
Title: Maximum Subarray Sum
https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/python

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list
of integers:
    max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.
Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""

def maxSequence(arr):
    contNegativo = 0
    somaAtual = 0
    listaSomas = []

    for i in range(0, len(arr)):   #EXCESSÕES
        if arr[i] < 0:
            contNegativo += 1
    if contNegativo == len(arr) or len(arr) == 0:
        return 0

    for i in arr[0:]:
        somaAtual += i
        if somaAtual < i:
            somaAtual = i
        listaSomas.append(somaAtual)
    #print(listaSomas)
    return max(listaSomas)



print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

