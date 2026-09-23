N-Rooks — Backtracking

Solves the N-Rooks problem using backtracking by placing one rook in each row and trying every possible column.

Approach
Place exactly one rook per row using recursion, so the row constraint is handled by construction.
For each candidate position, check whether another rook already exists above it in the same column.
Only the upward direction needs to be checked because the board is constructed top-to-bottom:
Current row has no rook yet → no left/right check required.
Future rows are empty → no downward check required.
Previous rows may contain rooks → check upward.
If the position is safe, place the rook and recursively process the next row.
After recursion returns, remove the rook to backtrack and try the next column.
When all N rows are processed, copy the board and store the solution.
Key Concepts

Backtracking · Recursion · Constraint Checking · Pruning · State Restoration · Deep Copy · Permutations

Since every row and column must contain exactly one rook, the complete solutions correspond to permutations of the N columns. Therefore, an N × N board has:

[N!] valid configurations.

For example:

N = 4 → 4! = 24 solutions
Complexity

The current implementation performs an upward column scan for each candidate, giving approximately O(N · N!) time, excluding detailed output-copying costs.

📖 Detailed Explanation:

https://www.notion.so/N-Rooks-Backtracking-3e44104ef5d48020af1efa6bec3632e9?source=copy_link