from typing import List

list_string = input('number list separate by ",": ').split(",")

k_i = int(input("k: "))

list_numbers = [int(n) for n in list_string]


def maxOperations(nums: List[int], k: int) -> int:
    response, i, e = 0, 0, len(nums) - 1
    nums.sort()
    while i < e:
        if nums[e] + nums[i] == k:
            i += 1
            e -= 1
            response += 1
        elif nums[e] + nums[i] > k:
            e -= 1
        else:
            i += 1

    return response


print(maxOperations(list_numbers, k_i))
