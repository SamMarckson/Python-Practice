"""
Title: Directions Reduction
Source: https://www.codewars.com/kata/550f22f4d758534c1100025a/python

Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST".
 Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild
 west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die
 of thirst!
How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following:
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So
 the task is to give to the man a simplified version of the plan. A better plan in this case is simply:
["WEST"]
Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).
"""


def dirReduc(a):

    def confereSeq(x):
        listaFinal = []
        for i in range(1, len(x)):
            if (x[i] == 'NORTH' and x[i-1] == 'SOUTH') or (x[i] == 'SOUTH' and x[i-1] == 'NORTH'):
                x[i] = ''
                x[i-1] = ''
            if (x[i] == 'EAST' and x[i-1] == 'WEST') or (x[i] == 'WEST' and x[i-1] == 'EAST'):
                x[i] = ''
                x[i-1] = ''

        for i in range(0, len(x)):
            if x[i] != '':
                listaFinal.append(x[i])

        for i in range(1, len(listaFinal)):
            if (listaFinal[i] == 'NORTH' and listaFinal[i - 1] == 'SOUTH') or (listaFinal[i] == 'SOUTH' and listaFinal[i - 1] == 'NORTH'):
                return confereSeq(listaFinal)
            if (listaFinal[i] == 'EAST' and listaFinal[i - 1] == 'WEST') or (listaFinal[i] == 'WEST' and listaFinal[i - 1] == 'EAST'):
                return confereSeq(listaFinal)

        return listaFinal

    return confereSeq(a)


#MAIN
print(dirReduc(["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"]))