input_string = input("copy a phrase: ")


def kidsWithCandies(s: str) -> str:
    response = s.split()
    response.reverse()
    return " ".join(response)

print(kidsWithCandies(input_string))
