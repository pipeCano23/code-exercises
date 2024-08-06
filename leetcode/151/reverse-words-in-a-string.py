input_string = input("copy a phrase: ")


def reverseWords(s: str) -> str:
    response = s.split()
    response.reverse()
    return " ".join(response)


print(reverseWords(input_string))
