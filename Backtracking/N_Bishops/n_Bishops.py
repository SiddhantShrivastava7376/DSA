import copy
from typing import List

def solveNBishops(n: int) -> List[List[str]]:

    board = [['.' for _ in range(n)] for _ in range(n)]
    row = 0
    col = 0
    solutions = []
    count = 0
    last_pos = pow(n, 2)


    def sol(row, col, count, board) -> None:

        curr_pos = row * n + col
        rem_pos = last_pos - curr_pos

        if count == n:

            result = copy.deepcopy(board)
            result = [''.join(r) for r in result]
            solutions.append(result)
            return

        if row == n: #no cells remain

            return

        if rem_pos < n - count: #remaining cells < remaining bishops needed

            return


        def isSafe(row, col, board) -> bool:

            a, b = row, col
            
            while a - 1 >= 0 and b- 1 >= 0: 

                if board[a - 1][b - 1] == 'B': #Check for upper left Digonal.

                    return False

                a -= 1
                b -= 1

            a, b = row, col

            while a - 1 >= 0 and b + 1 < n: #Check for upper right diagonal

                if board[a - 1][b + 1] == 'B':

                    return False

                a -= 1
                b += 1

            return True

        if isSafe(row, col, board):

            board[row][col] = 'B'
            count += 1

            if col + 1 < n:
                
                sol(row, col + 1, count, board)
                board[row][col] = '.'
                count -= 1
            else:
                sol(row + 1, 0, count, board)
                board[row][col] = '.'
                count -= 1

        if col + 1 < n: #No undo needed in the skip branch as we haven't place any bishop yet

            sol(row, col + 1, count, board)
        else:
            sol(row + 1, 0, count, board)

    sol(row, col, count, board)

    return solutions

n = 3

ans = solveNBishops(n)

print("All distinct solutions to the n-bishops puzzle are: ", ans)