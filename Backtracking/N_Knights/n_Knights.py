import copy
from typing import List

def solveNKnights(n: int) -> List[List[str]]:

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

        if rem_pos < n - count: #remaining cells < remaining knights needed

            return


        def isSafe(row, col, board) -> bool:

            if row - 1 >= 0 and col - 2 >= 0:

                if board[row - 1][col - 2] == 'K':

                    return False

            if row - 2 >= 0 and col - 1 >= 0:

                if board[row - 2][col - 1] == 'K':

                    return False
            
            if all(0 <= x < n for x in (row - 2, col + 1)):

                if board[row - 2][col + 1] == 'K':

                    return False
            
            if all(0 <= x < n for x in (row - 1, col + 2)):

                if board[row - 1][col + 2] == 'K':

                    return False

            return True

        if isSafe(row, col, board):

            board[row][col] = 'K'
            count += 1

            if col + 1 < n:
                
                sol(row, col + 1, count, board)
                board[row][col] = '.'
                count -= 1
            else:
                sol(row + 1, 0, count, board)
                board[row][col] = '.'
                count -= 1

        if col + 1 < n: #No undo needed in the skip branch as we haven't place any knight yet

            sol(row, col + 1, count, board)
        else:
            sol(row + 1, 0, count, board)

    sol(row, col, count, board)

    return solutions

n = 4

ans = solveNKnights(n)

print("All distinct solutions to the n-knights puzzle are: ", ans)