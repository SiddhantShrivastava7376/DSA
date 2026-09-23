import copy
from typing import List

def solveNQueens(n: int) -> List[List[str]]:

    board = [['.' for _ in range(n)] for _ in range(n)]
    row = 0
    solutions = []


    def sol(row, board) -> None:

        if row == n:

            result = copy.deepcopy(board)
            result = [''.join(r) for r in result]
            solutions.append(result)
            return


        def isSafe(row, col, board) -> bool:

                a, b = row, col

                while a - 1 >= 0 and b- 1 >= 0: 

                    if board[a - 1][b - 1] == 'Q': #Check for upper left Digonal.

                        return False

                    a -= 1
                    b -= 1

                a, b = row, col

                while a - 1 >= 0:

                    if board[a - 1][b] == 'Q': #Check for up.

                        return False

                    a -= 1

                a, b = row, col

                while a - 1 >= 0 and b + 1 < n: #Check for upper right diagonal

                    if board[a - 1][b + 1] == 'Q':

                        return False

                    a -= 1
                    b += 1

                return True

        for col in range(n):

            if isSafe(row, col, board):

                board[row][col] = 'Q'
                sol(row + 1, board)
                board[row][col] = '.'

    sol(row, board)

    return solutions

n = 4

ans = solveNQueens(n)

print("All distinct solutions to the n-queens puzzle are: ", ans)