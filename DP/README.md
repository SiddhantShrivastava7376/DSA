## LC-1312 — Minimum Insertion Steps to Make a String Palindrome

### Approach

Solved using **Top-Down Dynamic Programming (Memoization)** after first deriving a recursive solution.

I used two pointers, `i` and `j`, to represent the current substring `s[i...j]`.

The recursive state is:

```text
sol(i, j) = minimum insertions required to make s[i...j] a palindrome
```

### Recurrence

If the boundary characters match:

```text
s[i] == s[j]

→ sol(i + 1, j - 1)
```

If they don't match, either the left or right side can be handled with one insertion:

```text
1 + min(
    sol(i + 1, j),
    sol(i, j - 1)
)
```

Base case:

```text
i >= j → 0
```

### Optimization

The initial recursive solution had **overlapping subproblems**, causing TLE due to repeated computation.

I introduced a 2D memoization table:

```text
dp[i][j]
```

where each state stores the answer for substring `s[i...j]`.

The memoization pattern is:

```text
Check → Calculate → Store → Return
```

### Complexity

* **Time:** `O(n²)`
* **Space:** `O(n²)` for DP + `O(n)` recursion stack

### Concepts Used

* Recursion
* Two Pointers
* Interval DP
* Optimal Substructure
* Overlapping Subproblems
* Top-Down DP / Memoization

### Learning

The main progression was:

```text
Recursion
   ↓
TLE due to repeated states
   ↓
Identify state (i, j)
   ↓
Memoization
   ↓
O(n²) Top-Down DP
```

### Detailed Explanation

> **Notion:** 

https://www.notion.so/LC-1312-Minimum-Insertion-Steps-to-Make-a-String-Palindrome-3e94104ef5d4803792c7e10b258cba29?source=copy_link
