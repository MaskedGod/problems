"""If you are standing at step n, to get to this point, you must have either:
Taken a single step from n-1
Taken two steps from n-2
Thus, the total number of distinct ways to reach step n is the sum of the distinct ways to reach step n-1 and the distinct ways to reach step n-2.

This gives the recursive relation:

ways(n) = ways(n-1) + ways(n-2)"""


def climbStairs(n: int) -> int:
    memo = {}

    def steps(n: int) -> int:
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        memo[n] = steps(n - 1) + steps(n - 2)
        return memo[n]

    return steps(n)


# def climbStairsDp(n: int) -> int:
#     # Initialize the dp array with base cases
#     if n == 0:
#         return 1  # No steps, 1 way to stay at the bottom
#     if n == 1:
#         return 1  # Only 1 step, 1 way to climb

#     dp = [0] * (n + 1)  # Create a dp array of size n+1
#     dp[0] = 1  # 1 way to be at step 0 (doing nothing)
#     dp[1] = 1  # 1 way to reach step 1 (taking one step)

#     # Fill the dp array for steps 2 to n
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n]


def climbStairsDpOptimizes(n: int) -> int:
    # optimized for space
    # Base cases for 0 or 1 step
    if n == 0:
        return 1  # No steps, 1 way to stay at the bottom
    if n == 1:
        return 1  # Only 1 step, 1 way to climb

    # Initialize two variables to store the last two steps' results
    prev2 = 1  # This corresponds to dp[0]
    prev1 = 1  # This corresponds to dp[1]

    # Iterate from step 2 to n
    for i in range(2, n + 1):
        current = prev1 + prev2  # Number of ways to reach step i
        prev2 = prev1  # Move prev1 down to prev2
        prev1 = current  # Move current up to prev1

    return prev1  # The answer will be stored in prev1


# print(climbStairs(2), "--2ways")
# print(climbStairs(3), "--3ways")
# print(climbStairs(4), "--3ways")
print(climbStairsDpOptimizes(2), "--2ways")
print(climbStairsDpOptimizes(3), "--3ways")
print(climbStairsDpOptimizes(4), "--3ways")
print(climbStairsDpOptimizes(16), "--3ways")
