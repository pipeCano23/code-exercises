import math

str_1 = input("first str: ")
str_2 = input("second str: ")


def gcdOfStrings(str1: str, str2: str) -> str:
    limit1 = len(str1)
    limit2 = len(str2)

    if (limit1 == 0 or limit2 == 0) or (limit1 == limit2 and str1 != str2):
        return ""

    mcd = limit2
    aux = limit1

    while aux:
        mcd, aux = aux, mcd % aux

    gcp = str2[:mcd]

    repet1 = math.floor(limit1 / mcd)
    repet2 = math.floor(limit2 / mcd)

    compare1 = gcp * repet1
    compare2 = gcp * repet2

    if compare1 == str1 and compare2 == str2:
        return gcp

    return ""


print(gcdOfStrings(str_1, str_2))
