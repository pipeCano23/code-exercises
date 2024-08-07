s = input("s: ")
t = input("t: ")


def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True

    i, j = 0, 0
    response = False

    while i < len(t) and not response:
        if t[i] == s[j]:
            j += 1

        if j == len(s):
            response = True

        i += 1

    return response


print(isSubsequence(s, t))
