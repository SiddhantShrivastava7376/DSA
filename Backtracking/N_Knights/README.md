# N-Knights — Backtracking

### Problem

Place exactly `n` knights on an `n × n` chessboard such that no two knights attack each other, and generate all distinct valid configurations.

### Approach

I solved the problem using **Recursion + Backtracking + Constraint Checking + Pruning**.

Unlike N-Queens, I cannot place exactly one knight per row because knights do not attack horizontally. Therefore, I process the board **cell-by-cell** and make two decisions at every cell:

1. Place a knight.
2. Don't place a knight.

The recursive state is:

`sol(row, col, count, board)`

where `count` tracks the number of knights currently placed.

Before placing a knight, I check whether the current cell is safe. A knight has 8 possible attacking positions, but because the board is traversed in row-major order, only the 4 positions containing previously processed cells need to be checked:

- UL1 → `(row - 1, col - 2)`
- UL2 → `(row - 2, col - 1)`
- UR1 → `(row - 2, col + 1)`
- UR2 → `(row - 1, col + 2)`

After placing a knight, I recursively explore the next cell and then **undo the placement** during backtracking.

The search is also pruned when the number of remaining cells is insufficient to place the remaining knights.

### Core Pattern

`Place → Recurse → Undo`

and

`Skip → Recurse`

### Complexity

- Worst-case Time: `O(2^(n²))`
- Auxiliary Space: `O(n²)` excluding stored solutions.

### Key Concepts

- Recursion
- Backtracking
- Binary Decision Tree
- State Space Search
- Constraint Satisfaction
- Pruning
- Traversal Ordering
- Mutable State and Undo

### Detailed Explanation

[Notion — Detailed N-Knights Explanation]

https://www.notion.so/N-Knights-Backtracking-3e44104ef5d480a5a322e2a668a60129?source=copy_link