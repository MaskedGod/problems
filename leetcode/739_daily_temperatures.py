"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []

    for i in range(len(temperatures)):
        days = 0
        found_hotter = False

        for temp in temperatures[i + 1 :]:
            days += 1
            if temp > temperatures[i]:
                stack.append(days)
                found_hotter = True
                break

        if not found_hotter:
            stack.append(0)

    return stack


print(dailyTemperatures([30, 60, 90]))  # [1,1,0]
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
