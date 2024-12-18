def duplicate_encode(word: str) -> str:
    list_of_word = []
    for l in word:
        try:
            list_of_word.append(l.lower())
        except:
            list_of_word.append(l)

    res = ["(" if list_of_word.count(l) == 1 else ")" for l in list_of_word]
    return "".join(res)


# well .lower doesnt raise exceptions)) so yeah...
def duplicate_encode2(word):
    return "".join(
        ["(" if word.lower().count(c) == 1 else ")" for c in word.lower()]
    )


if __name__ == "__main__":
    print(duplicate_encode("(( @"))
