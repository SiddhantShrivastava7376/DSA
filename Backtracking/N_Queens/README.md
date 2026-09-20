## 1. Problem Statement

The **N-Queens problem** asks us to place `N` queens on an `N × N` chessboard such that **no two queens attack each other**.

A queen can attack another queen if they are in:

1. The same row
2. The same column
3. The same diagonal

For example, for `N = 4`, one valid configuration is:

```
. Q . .
. . . Q
Q . . .
. . Q .
```

Here, all four queens are placed such that no two queens attack each other.

The objective is to find **all distinct valid configurations**.

---

# 2. Main Approach Used

I solved the problem using:

> **Recursion + Backtracking + Constraint Checking**
> 

The main idea is:

> Place exactly one queen in each row, recursively move to the next row, and backtrack whenever a valid placement is no longer possible.
> 

Instead of trying every possible arrangement of `N` queens, I construct the solution **row by row**.

The overall strategy is:

```
Choose a position
      ↓
Check whether it is safe
      ↓
Place the queen
      ↓
Recursively solve the next row
      ↓
If recursion returns
      ↓
Remove the queen
      ↓
Try the next column
```

This is the fundamental **backtracking pattern**:

```
TRY → CHOOSE → EXPLORE → UNDO → TRY NEXT
```

---

# 3. Why One Queen Per Row?

A queen cannot share a row with another queen.

Therefore, if I ensure that every row gets exactly one queen, then I automatically eliminate the possibility of two queens attacking each other horizontally.

So instead of deciding:

> "Where should all N queens go?"
> 

I break the problem into smaller decisions:

> "Where should I place the queen in row 0?"
> 

Then:

> "Where should I place the queen in row 1?"
> 

Then:

> "Where should I place the queen in row 2?"
> 

And so on.

For `N = 4`:

```
Row 0 → place one queen
Row 1 → place one queen
Row 2 → place one queen
Row 3 → place one queen
```

Once I successfully place a queen in row `3`, I have a complete solution.

---

# 4. Why Recursion?

Recursion naturally represents the rows.

Each recursive call represents:

> "I have successfully placed queens in all previous rows. Now I need to solve this row."
> 

Conceptually:

```
sol(0)
  ↓
sol(1)
  ↓
sol(2)
  ↓
sol(3)
  ↓
sol(4)
```

For `N = 4`:

```
row = 0 → first queen
row = 1 → second queen
row = 2 → third queen
row = 3 → fourth queen
row = 4 → all queens placed
```

Therefore:

```
if row == n:
```

is my **base case**.

---

# 5. Why Backtracking?

Recursion alone is not enough.

Suppose I place a queen in a particular position:

```
Q . . .
. . . .
. . . .
. . . .
```

Then I recursively try to solve the remaining rows.

Suppose eventually I discover:

```
There is no valid position in the current row.
```

The previous decision must be reconsidered.

Therefore I:

```
Remove the previous queen
      ↓
Try another column
```

This is called **backtracking**.

The basic pattern in my code is:

```
board[row][col] = 'Q'
sol(row + 1, col, board)
board[row][col] = '.'
col += 1
```

This means:

```
PLACE
  ↓
RECURSE
  ↓
RETURN
  ↓
UNDO
  ↓
NEXT CHOICE
```

---

# 6. Decision Tree

The N-Queens problem can be viewed as a **decision tree**.

For `N = 4`, the first decision is:

> Where should the queen in row 0 be placed?
> 

There are four choices:

```
                    Row 0
                      |
          ┌───────────┼───────────┐
          ↓           ↓           ↓
        col 0       col 1       col 2       col 3
          |           |           |           |
          ↓           ↓           ↓           ↓
       Row 1       Row 1       Row 1       Row 1
```

Each child represents a possible choice for the next row.

However, **unsafe choices are immediately rejected**.

So the actual search tree is smaller than the complete set of possibilities.

---

# 7. Decision Tree for N = 4

Let's examine the search starting with row 0, column 0.

```
                         R0C0
                          |
                          Q
                          ↓
                       Row 1
                    /    |    \
                  C0     C1    C2    C3
                  ✗      ✗     ✓     ✓
                               |     |
                              ...   ...
```

The `✗` means the position is unsafe.

For example, after placing:

```
Q . . .
. . . .
. . . .
. . . .
```

row 1 cannot use column 0 because of the same column:

```
Q . . .
Q . . .   ← attacking vertically
```

It also cannot use column 1 because of the upper-left diagonal:

```
Q . . .
. Q . .  ← attacking diagonally
```

Therefore row 1 can try columns 2 and 3.

This is how **constraint checking prunes the decision tree**.

---

# 8. The `isSafe()` Function

Before placing a queen, I check whether the position is safe.

Because I place queens **from top to bottom**, there are already placed queens only in the rows above the current row.

Therefore, I only need to check three directions:

```
        ↖   ↑   ↗
             Q
```

I check:

1. Upper-left diagonal
2. Same column upward
3. Upper-right diagonal

I don't need to check:

```
↓
↙
↘
```

because there are no queens in the lower rows yet.

This is an important optimization.

---

# 9. Upper-Left Diagonal Check

For a candidate position `(row, col)`, I move:

```
row - 1
col - 1
```

repeatedly.

Conceptually:

```
Q . . .
. Q . .
. . X .
```

From `X`, I move:

```
↖
```

until I reach the boundary.

If I encounter:

```
'Q'
```

the candidate position is unsafe.

---

# 10. Same Column Check

I move upward while keeping the column unchanged:

```
Q . . .
. . . .
. . X .
```

From `X`:

```
↑
```

If I encounter a queen, the candidate is unsafe.

---

# 11. Upper-Right Diagonal Check

I move:

```
row - 1
col + 1
```

which corresponds to:

```
↗
```

For example:

```
. . . Q
. . X .
```

From `X`, I check upward-right.

Again, if I encounter a queen, the candidate is unsafe.

---

# 12. Why These Three Checks Are Sufficient

At any point in my algorithm:

```
Rows above → already processed
Current row → currently being processed
Rows below → empty
```

Therefore:

```
        Previously processed
        rows only
             ↓
       ↖    ↑    ↗
          current
          position
```

There cannot be a queen below the current row.

Also, because I place only one queen per row, horizontal checking is unnecessary.

Therefore the three checks are sufficient.

---

# 13. Complete Recursion Structure

My recursive function conceptually works like this:

```
sol(row)
   |
   ├── if row == N
   │       └── save solution
   │
   └── try every column
          |
          ├── Is position safe?
          |
          ├── NO
          │    └── try next column
          |
          └── YES
               |
               ├── place Q
               |
               ├── sol(row + 1)
               |
               ├── remove Q
               |
               └── try next column
```

This is the complete algorithm.

---

# 14. Dry Run for N = 4

Initial board:

```
. . . .
. . . .
. . . .
. . . .
```

We start with:

```
row = 0
```

---

## Step 1 — Row 0

Try column 0.

```
Q . . .
. . . .
. . . .
. . . .
```

It is safe.

Place the queen and recurse:

```
sol(1)
```

---

# 15. Row 1

Try column 0.

```
Q . . .
Q . . .
```

Unsafe because same column.

Reject it.

Next:

```
Q . . .
. Q . .
```

Unsafe because diagonal.

Reject it.

Next:

```
Q . . .
. . Q .
```

Safe.

Place it.

```
Q . . .
. . Q .
. . . .
. . . .
```

Recurse to row 2.

---

# 16. Row 2

Now try columns.

Column 0:

```
Q . . .
. . Q .
Q . . .
```

Unsafe because column 0 already contains a queen.

Column 1:

```
Q . . .
. . Q .
. Q . .
```

Unsafe diagonally with the queen at `(0,0)`.

Column 2:

```
Q . . .
. . Q .
. . Q .
```

Unsafe because column 2 is occupied.

Column 3:

```
Q . . .
. . Q .
. . . Q
```

This is also unsafe because it attacks the queen in row 1 diagonally.

Therefore:

```
No valid position in row 2
```

This is a **dead end**.

---

# 17. Backtracking Happens

We return to row 1.

The queen we placed at:

```
(row 1, col 2)
```

must be removed.

Before:

```
Q . . .
. . Q .
. . . .
. . . .
```

After undo:

```
Q . . .
. . . .
. . . .
. . . .
```

Now row 1 tries its next column:

```
col = 3
```

Place:

```
Q . . .
. . . Q
. . . .
. . . .
```

Then recurse to row 2.

This demonstrates why the statement:

```
board[row][col] = '.'
```

is so important.

It allows the algorithm to return to an earlier decision and explore another possibility.

---

# 18. Eventually a Solution Is Found

One of the valid configurations discovered is:

```
. Q . .
. . . Q
Q . . .
. . Q .
```

Represented as:

```
".Q.."
"...Q"
"Q..."
"..Q."
```

When the algorithm places the fourth queen successfully, it calls:

```
sol(4)
```

Since:

```
row == n
```

the base case executes.

The current board is copied and stored.

---

# 19. Why `deepcopy()` Is Used

The board is continuously modified during backtracking.

Suppose I save:

```
.Q..
...Q
Q...
..Q.
```

Then the algorithm continues and performs:

```
board[row][col] = '.'
```

If I had stored the same board object, the saved solution could also change.

Therefore I create an independent copy:

```
result = copy.deepcopy(board)
```

Then:

```
solutions.append(result)
```

The saved configuration is now independent of the working board.

---

# 20. The Two Solutions for N = 4

The algorithm eventually finds the two distinct configurations:

### Solution 1

```
.Q..
...Q
Q...
..Q.
```

### Solution 2

```
..Q.
Q...
...Q
.Q..
```

These are the two solutions for `N = 4`.

---

# 21. Complete Conceptual Recursion Tree

A simplified view of the search is:

```
                         Row 0
                    /      |      |      \
                  C0       C1     C2       C3
                  |        |      |        |
                Row 1    Row 1   Row 1    Row 1
              / | \ \    ...     ...    / | \ \
             ...          |       |       ...
                           ↓
                        Row 2
                      / / | \
                     ✗ ✗  ✗  ...
                           |
                        dead end
                           |
                        BACKTRACK
                           ↑
                      undo previous Q
                           |
                     try next column
```

The important point is that this is **not simply a tree where every branch reaches the bottom**.

Many branches terminate early because `isSafe()` rejects positions.

Therefore, backtracking **prunes** the search space.

---

# 22. Decision Tree vs Recursion Tree

### Decision Tree

Represents the **choices** being made:

```
Row 0:
    choose column 0
    choose column 1
    choose column 2
    choose column 3
```

Then for each choice:

```
Row 1:
    choose column 0
    choose column 1
    choose column 2
    choose column 3
```

It represents the possible decisions.

### Recursion Tree

Represents the actual recursive execution:

```
sol(0)
  |
  +-- sol(1)
       |
       +-- sol(2)
            |
            +-- sol(3)
                 |
                 +-- sol(4)
```

Some recursive branches terminate early because their candidate positions are unsafe.

In practice, the two views overlap heavily in backtracking problems.

---

# 23. Why This Is Backtracking Rather Than Just Recursion

The critical difference is the **undo step**.

Without:

```
board[row][col] = '.'
```

once I placed a queen, it would remain permanently on the board.

Then the algorithm couldn't reconsider previous decisions.

Backtracking gives the algorithm the ability to say:

> "This choice didn't lead to a solution. I'll undo it and try another choice."
> 

Therefore:

```
Recursion:
    Make a choice
    Explore deeper

Backtracking:
    Make a choice
    Explore deeper
    Undo the choice
    Try another choice
```

---

# 24. State of the Algorithm

At any point, the board represents the **current partial solution**.

For example:

```
Q . . .
. . Q .
. . . .
. . . .
```

means:

```
Row 0 → column 0 chosen
Row 1 → column 2 chosen
Rows 2 and 3 → not decided yet
```

So the board itself is part of the current recursive state.

---

# 25. Complexity

The straightforward search has a large exponential search space.

If we ignored constraints and allowed every column choice independently, there would be approximately:

```
N × N × N × ... × N
```

choices:

```
N^N
```

However, because we place only one queen per row and reject unsafe positions early, the actual search is substantially pruned.

A common upper-bound discussion for the standard backtracking solution is:

```
O(N!)
```

for the search space when considering one queen per row and distinct columns.

The safety check in your implementation scans up to `O(N)` positions.

Therefore, a simple conservative complexity description for your implementation is often given around:

```
O(N × N!)
```

depending on how the branching and safety-check costs are accounted for.

The exact practical runtime is much better than blindly enumerating all `N^N` boards because invalid branches are cut off early.

---

# 26. Space Complexity

The board requires:

```
O(N²)
```

space.

The recursion depth is:

```
O(N)
```

because at most one recursive call exists for each row.

The solutions themselves require additional space proportional to the number of solutions and the size of each board.

So excluding the output:

```
Auxiliary space ≈ O(N² + N)
```

which is effectively:

```
O(N²)
```

for the board.

Including the output, the total space also depends on the number of valid N-Queens configurations.

---

# 27. Important Concepts I Learned from This Problem

This N-Queens problem helped me apply several important DSA concepts.

### 1. Recursion

Each recursive call handles the next row.

```
row → row + 1
```

### 2. Backtracking

After exploring a choice:

```
place → recurse → undo
```

### 3. Constraint Checking

Before making a decision, I check whether it violates the constraints.

```
isSafe(row, col)
```

### 4. State Management

The board represents the current state of the search.

### 5. Base Case

```
if row == n:
```

means a complete valid configuration has been constructed.

### 6. Deep Copy

The solution must be stored independently from the mutable working board.

### 7. Search-Space Pruning

Unsafe choices are rejected immediately instead of exploring their entire subtree.

## Final Takeaway

The most important thing I learned from implementing N-Queens is that **backtracking is not simply recursion**.

Recursion takes me forward:

```
current choice → next row
```

Backtracking allows me to come back:

```
next row fails
      ↓
undo previous choice
      ↓
try another choice
```

Therefore, the fundamental pattern I implemented is:

> **Choose → Check → Explore → Undo → Try Next**
> 

This same pattern can be applied to many other problems such as **Rat in a Maze, N-Queens, Sudoku, graph coloring, Hamiltonian cycle, subset generation, and permutation problems**.