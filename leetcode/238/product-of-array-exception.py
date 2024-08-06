from typing import List

list_string = input('numbers list separate by ",": ').split(",")

list_numbers = [int(n) for n in list_string]


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix, postfix = 1, 1  # init in one
    prod_left, prod_right = [], []  # save product

    for i, n in enumerate(nums):
        prod_left.append(prefix)
        prefix *= n
        prod_right.append(postfix)
        postfix *= nums[len(nums) - 1 - i]

    result = []
    for i, _ in enumerate(nums):
        prod_result = prod_left[i] * prod_right[len(nums) - 1 - i]
        result.append(prod_result)

    return result


print(productExceptSelf(list_numbers))
