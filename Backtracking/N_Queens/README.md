# N-Queens

### Problem

Place `N` queens on an `N × N` chessboard such that no two queens attack each other, and return all distinct valid configurations.

### Approach

I solved the problem using **Recursion + Backtracking + Constraint Checking**.

* Place exactly **one queen per row**.
* For each row, try every possible column.
* Before placing a queen, check whether the position is safe by checking:

  * Upper-left diagonal ↖
  * Same column ↑
  * Upper-right diagonal ↗
* If the position is safe, place the queen and recursively solve the next row.
* After the recursive call returns, **remove the queen** and try the next column.
* When `row == n`, a complete valid configuration has been found. A deep copy of the board is stored in the solutions list.

### Core Backtracking Pattern

```text
Choose → Check → Place → Recurse → Undo → Try Next
```

### Key Concepts

* Recursion and recursive state
* Backtracking
* Constraint checking
* Search-space pruning
* Base cases
* Mutable-state management and `deepcopy()`

### Complexity

* **Time:** Approximately `O(N × N!)` for this implementation
* **Auxiliary Space:** `O(N²)` excluding the output

### Detailed Explanation

For the complete **recursion tree, decision tree, dry run, and detailed explanation of the approach**, see my Notion notes:

🔗 **[Detailed N-Queens Notes — Notion]

https://www.notion.so/N-Queens-Problem-Complete-Explanation-of-My-Approach-32c4104ef5d48031b9c5cf5a28270a09?source=copy_link
