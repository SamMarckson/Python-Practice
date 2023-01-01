"""
TITLE: Matrix Determinant
SOURCE: https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
How to take the determinant of a matrix -- it is simplest to start with the smallest cases:
A 1x1 matrix |a| has determinant a.
A 2x2 matrix [ [a, b], [c, d] ] has determinant: a*d - b*c.
The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants
of n matrices ofn-1 x n-1 size.
For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] the determinant is:
a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2
matrix created by crossing out the row and column in which the element a occurs:
Note the alternation of signs.
The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d],
then:
det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
"""

import numpy

def determinant(matrix):

    if len(matrix) == 1:
        return matrix[0][0]

    return round(numpy.linalg.det(matrix))


#MAIN
print(determinant([[4, 6], [3, 8]]))
#print(determinant([[2, 4, 2], [3, 1, 1], [1, 2, 0]]))
#print(determinant([[4]]))
#print(determinant([[1, 0, 1, 8], [1, 2, 0, 3], [4, 6, 2, 6], [0, 3, 6, 4]]))