def count_substring(string, sub_string):
    s = 0
    for i in range(len(string)):
        s += string[i : i + len(sub_string)].count(sub_string)
    return s


if __name__ == "__main__":
    string = input("$: ").strip()
    sub_string = input("$:").strip()

    # Sample
    string = "ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)
