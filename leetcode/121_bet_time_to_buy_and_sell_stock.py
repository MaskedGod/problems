def maxProfit(prices: list[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    # Time: O(n)
    # Space: O(1)
    if not prices:
        return 0
    buy = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        if prices[i] - buy > profit:
            profit = prices[i] - buy

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]), "5")
print(maxProfit([1, 2]), "1")
print(maxProfit([2, 4, 1]), "2")
print(maxProfit([7, 6, 4, 3, 1]), "0")
