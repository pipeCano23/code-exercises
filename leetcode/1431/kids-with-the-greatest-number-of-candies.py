from typing import List

list_string = input('numbers list separate by ",": ').split(",")

list_candies = [int(n) for n in list_string]

extra_candies = int(input("Extra candies: "))


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)

    return [(c + extraCandies) >= max_candies for c in candies]


print(kidsWithCandies(list_candies, extra_candies))
