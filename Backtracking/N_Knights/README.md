N-Knights — Approach, Recursion Tree, Decision Tree & Dry Run
1. Problem

The goal is to place exactly n knights on an n × n chessboard such that no two knights attack each other, and generate all valid configurations.

A knight attacks a square that is:

2 rows and 1 column away, or
1 row and 2 columns away.

Therefore, each knight has at most 8 possible attacking positions.

2. Approach Used

I solved the problem using Backtracking with Recursion.

Unlike N-Queens, where I can place one queen per row because queens attack horizontally, I cannot restrict knights to one per row because two knights in the same row do not attack each other.

Therefore, I traverse the board cell by cell in row-major order:

(0,0) → (0,1) → (0,2) → ... → (1,0) → (1,1) → ...

At every cell, I have two choices:

Place a knight
Don't place a knight

The recursive state is:

sol(row, col, count, board)

where:

row, col → current cell
count → number of knights currently placed
board → current board configuration
3. Decision Tree

At every cell, the recursion creates two branches:

                         Current Cell
                         /          \
                   PLACE K         DON'T PLACE
                      |                 |
                  count + 1            count
                      |                 |
                  Next Cell          Next Cell

For example, starting at (0,0):

                         (0,0)
                       /       \
                    Place       Skip
                     K           .
                    /             \
                 (0,1)           (0,1)
                /     \         /     \
             Place   Skip     Place   Skip

The algorithm continues exploring both possibilities until either:

count == n → valid solution found
all cells are exhausted → branch fails
remaining cells are insufficient to place the remaining knights → prune branch
4. Important Optimization in isSafe()

Initially, there are 8 possible attacking positions around a knight.

However, because I traverse the board in row-major order, when checking the current cell, only positions that have already been visited can contain previously placed knights.

Therefore, I only need to check the four upper attacking positions:

             UL2       UR1
                \     /
                 \   /
                  X       ← current cell
                 / \
                /   \
             UL1     UR2

Specifically:

UL1 = (row - 1, col - 2)
UL2 = (row - 2, col - 1)
UR1 = (row - 2, col + 1)
UR2 = (row - 1, col + 2)

The four lower positions don't need to be checked because those cells haven't been visited yet.

This reduces the safety checking from 8 potential positions to 4.

5. Boundary Checking

Before accessing any of those four positions, I verify that the position is actually inside the board.

For example:

(row - 1, col - 2)

is checked only if:

0 ≤ row - 1 < n
0 ≤ col - 2 < n

This is particularly important in Python because negative indices can refer to elements from the end of a list rather than immediately producing an error.

6. Base Cases and Pruning
Success
count == n

means exactly n knights have been placed.

So I:

copy the board
convert rows to strings
store the solution
return
Failure

If:

row == n

then every cell has been processed but fewer than n knights were placed.

Therefore, this branch cannot produce a solution.

Pruning

I also calculate the number of cells remaining.

If:

remaining cells < n - count

then even if I put a knight on every remaining cell, I still cannot reach n knights.

Therefore, I immediately terminate that branch.

This is pruning, which avoids unnecessary recursive exploration.

7. Dry Run — n = 2

Consider:

n = 2

We need to place exactly 2 knights.

Initially:

. .
. .

State:

row = 0
col = 0
count = 0
Cell (0,0)

There are no previously visited attacking positions.

So the cell is safe.

We have two possibilities.

Branch 1 — Place
K .
. .

Now:

count = 1

Move to (0,1).

At (0,1), there are still no previously placed knights attacking it.

Place:

K K
. .

Now:

count = 2

Therefore:

count == n

So this is a valid solution.

Backtrack

Remove the knight from (0,1):

K .
. .

Then explore the SKIP branch for (0,1).

Continue to (1,0).

Possible configuration:

K .
K .

Again, there are two knights and they don't attack each other.

So another solution is found.

The recursion continues exploring every remaining combination.

8. Backtracking Mechanism

The core operation is:

PLACE
  ↓
RECURSE
  ↓
UNDO

For example:

. . . .
. . . .
. . . .
. . . .

Place:

K . . .
. . . .
. . . .
. . . .

Explore all possibilities that begin with that placement.

After returning:

K → .

and the board becomes:

. . . .
. . . .
. . . .
. . . .

Now the algorithm can explore the alternative:

DON'T PLACE

This place → explore → undo mechanism is the essence of backtracking.

9. Overall Recursion Tree

Conceptually, the recursion tree looks like:

                         Cell (0,0)
                       /           \
                   PLACE           SKIP
                     |               |
                Cell (0,1)       Cell (0,1)
                /       \         /       \
             PLACE     SKIP    PLACE     SKIP
               |         |       |         |
             ...       ...     ...       ...
               \         |       |         /
                \        |       |        /
                  Valid / Invalid branches

The tree continues until:

                 ┌───────────────┐
                 │ count == n    │
                 │   SUCCESS     │
                 └───────────────┘

                         OR

                 ┌───────────────┐
                 │ row == n      │
                 │   FAILURE     │
                 └───────────────┘

Branches that cannot possibly place the remaining knights are pruned early.

10. Underlying DSA Concepts Used

The solution combines several important concepts:

1. Recursion

The function calls itself to solve the remaining board cells.

2. Backtracking

After exploring a placement, the knight is removed so that another possibility can be explored.

Place → Explore → Undo
3. State Space Tree

Every cell creates two possible decisions:

Place / Don't Place

which forms a binary decision tree.

4. Constraint Checking

Before placing a knight, isSafe() verifies that no previously placed knight attacks the current cell.

5. Pruning

Branches that cannot possibly reach n knights are terminated early.

remaining cells < remaining knights needed
6. Search-order Optimization

Because I traverse row-by-row, I only check the four attacking positions that could already contain knights rather than all eight possible positions.

Final Summary

My solution follows this pattern:

Traverse every cell
       ↓
Two choices:
PLACE / DON'T PLACE
       ↓
If PLACE:
    check knight constraints
       ↓
    place knight
       ↓
    recurse with count + 1
       ↓
    undo placement
       ↓
Explore DON'T PLACE branch
       ↓
Prune impossible branches
       ↓
When count == n:
    store solution

The key difference from my N-Queens solution is that I cannot assume one knight per row. Therefore, instead of making one decision per row, I make two decisions for every cell. The combination of recursion, backtracking, constraint checking, and pruning allows me to systematically explore all valid N-Knights configurations.