word_1 = input("first word: ")
word_2 = input("second word: ")


def mergeAlternately(word1: str, word2: str) -> str:
    if len(word1) == 0 or len(word2) == 0:
        return word1 + word2

    idx1 = 0
    idx2 = 0
    response = ""

    while idx1 < len(word1) and idx2 < len(word2):
        response += word1[idx1] + word2[idx2]
        idx1 += 1
        idx2 += 1

    return response + word1[idx1:] + word2[idx2:]


print(mergeAlternately(word_1, word_2))
