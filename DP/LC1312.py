def minInsertions(s: str) -> int:

        n = len(s)
        i = 0
        j = n - 1
        dp = [[-1 if i <= j else 0 for j in range(n)] for i in range(n)]

        def sol(i, j, dp) -> int:

            if i >= j:

                return 0

            if dp[i][j] != -1:

                return dp[i][j]

            if s[i] == s[j]:

                result =  sol(i + 1, j - 1, dp)
                dp[i][j] = result #Store in dp
                return result
            else:
                count1 = 1 + sol(i + 1, j, dp)
                count2 = 1 + sol(i, j - 1, dp)
                result = min(count1, count2)
                dp[i][j] = result #Store in dp
                return result

        return sol(i, j, dp)

s = "leetcode"

print("Minimum number of steps to make s palindrome is: ", minInsertions(s))