"""
Title: By the Power Set of Castle Grayskull
Source: https://www.codewars.com/kata/53d3173cf4eb7605c10001a8/python

Write a function that returns all of the sublists of a list/array.

Example:
power([1,2,3]);=>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]power([1,2,3]);
"""

from itertools import combinations

def power(a):
    lst = []
    for i in range(1, len(a)+1):
        comb = combinations(a, i)
        for j in comb:
            lst.append(list(j))
    lst.insert(0, [])
    return lst

#MAIN
print(power([1, 2, 3]))