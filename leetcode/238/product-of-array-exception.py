from typing import List
from functools import reduce

list_string = input('numbers list separate by ",": ').split(",")

list_numbers = [int(n) for n in list_string]


def kidsWithCandies(nums: List[int]) -> List[int]:
    result = []
    for i, _ in enumerate(nums):
        if i == 0:
            result.append(reduce((lambda x, y: x * y), nums[i + 1 :]))
        elif i == (len(nums) - 1):
            result.append(reduce((lambda x, y: x * y), nums[:i]))
        else:
            result.append(reduce((lambda x, y: x * y), nums[:i] + nums[i + 1 :]))
    return result


print(kidsWithCandies(list_numbers))
