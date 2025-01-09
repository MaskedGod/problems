"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

# def dailyTemperatures(temperatures: list[int]) -> list[int]:
#     stack = []

#     for i in range(len(temperatures)):
#         days = 0
#         found_hotter = False

#         for temp in temperatures[i + 1 :]:
#             days += 1
#             if temp > temperatures[i]:
#                 stack.append(days)
#                 found_hotter = True
#                 break

#         if not found_hotter:
#             stack.append(0)

#     return stack

# def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#     answer = [0] * len(temperatures)
#     warmest_temp = temperatures[-1]
#     for day in range(len(temperatures) - 2, -1, -1):
#         temp = temperatures[day]
#         if temp >= warmest_temp:
#             warmest_temp = temp
#         else:
#             next_day = day + 1
#             while temperatures[next_day] <= temp:
#                 next_day += answer[next_day]
#             answer[day] = next_day - day
#     return answer


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    days_stk: This stores the result, initialized with 0 because by default, if no warmer day is found, the result should be 0.

    ind_stk: This stores the indices of unresolved temperatures, i.e., temperatures that haven't yet found a warmer day.

    The loop: As you iterate through the temperatures:

    The while loop checks if the current temperature is warmer than the temperature at the index stored at the top of the stack. If it is, you resolve that index by setting days_stk[top] = i - top (i.e., how many days it took to find a warmer temperature).
    The index i is then pushed onto the stack to potentially be resolved later.
    """
    temp_length = len(temperatures)
    ind_stk = []
    days_stk = [0] * temp_length

    for i in range(temp_length):

        while ind_stk and temperatures[i] > temperatures[ind_stk[-1]]:
            top = ind_stk.pop()
            days_stk[top] = i - top

        ind_stk.append(i)

    return days_stk


print(dailyTemperatures([30, 60, 90]))  # [1,1,0]
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
