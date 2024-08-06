from typing import List

flowered_string = input('numbers list separate by ",": ').split(",")

flowered_list = [int(n) for n in flowered_string]

input_n = int(input("n: "))


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    if (len(flowerbed) == 1 and flowerbed[0] != 1) or n == 0:
        return True

    response = False

    count = 0
    i = 0
    while i < (len(flowerbed)) and not response:
        if (
            flowerbed[i] != 1
            and (i + 1) < len(flowerbed)
            and (
                (i == 0 and flowerbed[i + 1] != 1)
                or (i > 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1)
            )
        ):
            flowerbed[i] = 1
            count += 1

        if (i + 1) == len(flowerbed) and flowerbed[i] != 1 and flowerbed[i - 1] != 1:
            flowerbed[i] = 1
            count += 1

        if count >= n:
            response = True

        i += 1

    return response


print(canPlaceFlowers(flowered_list, input_n))
