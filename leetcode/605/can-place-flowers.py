from typing import List

flowered_string = input('numbers list separate by ",": ').split(",")

flowered_list = [int(n) for n in flowered_string]

input_n = int(input("n: "))


def kidsWithCandies(flowered: List[int], n: int) -> bool:

    if (len(flowered) == 1 and flowered[0] != 1) or n == 0:
        return True

    response = False

    count = 0
    i = 0
    while i < (len(flowered) - 1) and not response:
        if (
            flowered[i] != 1
            and (i + 1) < len(flowered)
            and (
                (i == 0 and flowered[i + 1] != 1)
                or (i > 0 and flowered[i - 1] != 1 and flowered[i + 1] != 1)
            )
        ):
            count += 1

        if count >= n:
            response = True

        i += 1

    return response


print(kidsWithCandies(flowered_list, input_n))
