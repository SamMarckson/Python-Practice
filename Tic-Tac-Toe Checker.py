"""
Title: Tic-Tac-Toe Checker
Source: https://www.codewars.com/kata/525caa5c1bf619d28c000335/python
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we?
 Our goal is to create a function that will check that for us!
Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2
 if it is an "O", like so:
    [[0, 0, 1],
     [0, 1, 2],
     [2, 1, 0]]
We want our function to return:
    -1 if the board is not yet finished AND no one has won yet (there are empty spots),
    1 if "X" won,
    2 if "O" won,
    0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""


def is_solved(board):
    contadorDeZero = 0

    for i in range(0, 3):                       #VERIFICANDO AS LINHAS
        contLinha_1, contLinha_2 = 0, 0
        for j in range(0, 3):
            if board[i][j] == 1:
                contLinha_1 += 1
            if board[i][j] == 2:
                contLinha_2 += 1
            if board[i][j] == 0:
                contadorDeZero = -1
        if contLinha_1 == 3:
            return 1
        elif contLinha_2 == 3:
            return 2

    for j in range(0, 3):                       #VERIFICANDO AS COLUNAS
        contColuna_1, contColuna_2 = 0, 0
        for i in range(0, 3):
            if board[i][j] == 1:
                contColuna_1 += 1
            if board[i][j] == 2:
                contColuna_2 += 1
            if board[i][j] == 0:
                contadorDeZero = -1
        if contColuna_1 == 3:
            return 1
        elif contColuna_2 == 3:
            return 2

    listaDiagAscendente = [board[2][0], board[1][1], board[0][2]]
    listaDiagDescendente = [board[0][0], board[1][1], board[2][2]]

    if 0 not in listaDiagAscendente:
        if (listaDiagAscendente[0] == listaDiagAscendente[1]) and (listaDiagAscendente[0] == listaDiagAscendente[2]):           #VERIFICANDO A DIAGONAL ASC
            return listaDiagAscendente[0]

    if 0 not in listaDiagDescendente:
        if (listaDiagDescendente[0] == listaDiagDescendente[1]) and (listaDiagDescendente[0] == listaDiagDescendente[2]):       #VERIFICANDO A DIAGONAL DESC
            return listaDiagDescendente[0]

    if contadorDeZero == -1:        #CASO EM QUE HÁ ESPAÇO VAZIO
        return -1
    else:                           #CASO EM QUE HÁ EMPATE
        return 0


#MAIN
print(is_solved([[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]))