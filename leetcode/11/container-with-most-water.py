from typing import List

list_string = input('heights list separate by ",": ').split(",")

list_numbers = [int(n) for n in list_string]


def maxArea(height: List[int]) -> int:
    p1, p2, a = 0, (len(height) - 1), 0
    while p1 < p2:
        currentArea = min(height[p1], height[p2]) * (p2 - p1)
        if a < currentArea:
            a = currentArea
        if height[p1] < height[p2]:
            p1 += 1
        elif height[p1] > height[p2]:
            p2 -= 1
        else:
            if height[p1 + 1] > height[p2 - 1]:
                p1 += 1
            else:
                p2 -= 1

    return a


print(maxArea(list_numbers))
