N-Bishops — Backtracking
Approach

I solved the N-Bishops problem using backtracking with cell-by-cell traversal.

Instead of placing one bishop per row, I examine every cell of the N × N board and make an include/exclude decision:

Current Cell
   /      \
Place     Skip
  |         |
isSafe?   Next Cell
  |
Place Bishop
  |
Recurse
  |
Undo

A bishop attacks only along diagonals. Since the board is traversed in row-major order, when checking a new cell I only need to inspect the upper-left and upper-right diagonals for previously placed bishops.

Backtracking

When a cell is safe:

Place Bishop
    ↓
count++
    ↓
Explore next cell
    ↓
Remove Bishop
    ↓
count--

The skip branch requires no undo because the board is not modified.

Base Cases & Pruning
count == N → a valid configuration is found.
row == N → no cells remain, so the branch terminates.
If the number of remaining cells is smaller than the number of bishops still required, the branch is pruned.
Key Concepts
Recursion
Backtracking
Include/Exclude decision tree
Constraint checking
Diagonal traversal
State management
Pruning
Deep copying of solutions
Relation to Previous Problems

The approach combines ideas from my previous backtracking problems:

N-Knights
→ cell-by-cell traversal + include/exclude

N-Queens
→ diagonal safety checking

N-Bishops
→ cell traversal + diagonal constraint + backtracking

The main learning is that the backtracking pattern depends on how the problem's state and choices are represented. Here, each board cell represents a binary decision: place a bishop or skip it.

## Detailed Notes

For detailed explanation, recursion tree, decision tree,
dry run, and problem-solving process:

[📖 Read my detailed Notion notes]

https://www.notion.so/N-Bishops-Backtracking-Approach-3e44104ef5d480d88251e2017df91d6a?source=copy_link