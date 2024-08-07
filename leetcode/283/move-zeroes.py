from typing import List

def moveZeroes(nums: List[int]) -> None:
    i, p = 0, None
    while i < len(nums):
        if nums[i] == 0 and p == None:
            p = i

        if nums[i] != 0 and p != None:
            aux = nums[i]
            nums[i] = nums[p]
            nums[p] = aux
            i = p + 1
            p = None
        else:
            i += 1
