### What is **Dynamic Programming (DP)?**
Dynamic Programming is a technique used to solve problems by breaking them down into smaller subproblems. The key idea is to store the results of subproblems (either using memoization or tabulation) so that we don't have to recompute them. It helps in solving optimization problems efficiently.

There are two main strategies:
1. **Memoization**: This is a top-down approach where the result of each subproblem is stored in memory so that it can be reused when needed.
2. **Tabulation**: This is a bottom-up approach where the solution is built from smaller subproblems stored in a table (like an array).

Now, let's go over each of the classic DP problems.

---

### 1. **Fibonacci Sequence**
   - **How it works**:
     - The Fibonacci sequence is defined as: 
       - `Fib(0) = 0`
       - `Fib(1) = 1`
       - `Fib(n) = Fib(n-1) + Fib(n-2)` for `n >= 2`
     - Without memoization, calculating the Fibonacci sequence leads to redundant calculations. With DP, we can store previous results to avoid recalculating them.
     - **Efficiency**: Without DP, the time complexity is O(2^n). With memoization or tabulation, it reduces to O(n).

   - **Memoization Example**:
     In this approach, we store previously computed Fibonacci numbers to reuse them.

   **Python Code (Memoization)**:
   ```python
   def fibonacci(n, memo={}):
       if n in memo:
           return memo[n]  # Return cached result

       if n <= 1:
           return n

       # Store result in memo before returning
       memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
       return memo[n]

   # Example
   print(fibonacci(10))  # Output: 55 (Fib(10) = 55)
   ```

   - **Tabulation Example**:
     In this approach, we iteratively calculate Fibonacci numbers and store them in a table.

   **Python Code (Tabulation)**:
   ```python
   def fibonacci(n):
       if n <= 1:
           return n
       
       fib = [0] * (n + 1)
       fib[1] = 1

       for i in range(2, n + 1):
           fib[i] = fib[i-1] + fib[i-2]

       return fib[n]

   # Example
   print(fibonacci(10))  # Output: 55
   ```

---

### 2. **Longest Common Subsequence (LCS)**
   - **How it works**:
     - The problem is to find the longest subsequence that appears in both strings (not necessarily continuous).
     - Example: For strings `"abcde"` and `"ace"`, the LCS is `"ace"` (length 3).
     - The key idea is to use a 2D table to store results of subproblems. If characters match, we add 1 to the previous result; otherwise, we take the maximum of excluding either character.
     - **Efficiency**: Time complexity is O(n * m), where n and m are the lengths of the two strings.

   - **Example Explanation**:
     - For `"abcde"` and `"ace"`:
       - Compare the first letters: `'a'` and `'a'` → Match, so add 1 to the result.
       - Move to next characters and repeat the process.

   **Python Code (Tabulation)**:
   ```python
   def lcs(X, Y):
       m = len(X)
       n = len(Y)

       # Create a 2D table to store lengths of longest common subsequences
       dp = [[0] * (n + 1) for _ in range(m + 1)]

       # Build the dp table in a bottom-up manner
       for i in range(1, m + 1):
           for j in range(1, n + 1):
               if X[i - 1] == Y[j - 1]:
                   dp[i][j] = dp[i - 1][j - 1] + 1
               else:
                   dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

       return dp[m][n]  # The last element contains the length of LCS

   # Example
   X = "abcde"
   Y = "ace"
   print(lcs(X, Y))  # Output: 3 (LCS is "ace")
   ```

---

### 3. **0/1 Knapsack Problem**
   - **How it works**:
     - The problem is to maximize the value of items you can carry in a knapsack with a weight limit. Each item has a value and a weight, and you must decide whether to include it in the knapsack (0/1 decision for each item).
     - If you include an item, you reduce the remaining capacity; otherwise, you skip it. The goal is to find the optimal set of items that maximizes the total value without exceeding the weight limit.
     - **Efficiency**: Time complexity is O(n * W), where `n` is the number of items and `W` is the capacity of the knapsack.

   - **Example Explanation**:
     - You have items with weights `[2, 3, 4]` and values `[4, 5, 6]`, and a knapsack with capacity `5`.
     - For each item, you either take it or leave it based on its weight and value. 
     - For instance, if you include the second item (weight 3, value 5), you have a remaining capacity of 2. You then decide whether to take any more items within the remaining capacity.

   **Python Code (Tabulation)**:
   ```python
   def knapsack(weights, values, capacity):
       n = len(values)

       # Create a 2D dp array, dp[i][j] represents max value for i items and capacity j
       dp = [[0] * (capacity + 1) for _ in range(n + 1)]

       # Build the dp array
       for i in range(1, n + 1):
           for w in range(1, capacity + 1):
               if weights[i - 1] <= w:
                   dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
               else:
                   dp[i][w] = dp[i - 1][w]

       return dp[n][capacity]  # The last element contains the max value for full capacity

   # Example
   weights = [2, 3, 4]
   values = [4, 5, 6]
   capacity = 5
   print(knapsack(weights, values, capacity))  # Output: 9
   ```

---

### Summary of **Dynamic Programming** Algorithms:
1. **Fibonacci Sequence**: Solve recursively or iteratively by reusing previously calculated values (memoization or tabulation).
2. **Longest Common Subsequence (LCS)**: Use a 2D table to store lengths of subsequences and build the solution incrementally.
3. **0/1 Knapsack**: Maximize value while adhering to a weight limit using a table to store subproblem results.

These problems show the power of DP in optimizing recursive solutions by avoiding redundant calculations, making them more efficient.
