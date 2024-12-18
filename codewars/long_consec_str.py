a = ["zone", "abigail", "theta", "form", "libe", "zas"]
k = 2


def longest_consec(strarr, k):
    longest = " "
    long = " "

    if k > len(strarr) or k <= 0:
        return longest

    for ind, string in enumerate(strarr):

        if k > 1:
            long = string
            for _ in range(k - 1):
                ind += 1
                if ind >= len(strarr):
                    continue
                else:
                    long += strarr[ind]
        else:
            long = string

        if len(long) > len(longest):
            longest = long

    return longest


def longest_consecutive(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = "".join(strarr[index : index + k])
            if len(s) > len(result):
                result = s

    return result


print(longest_consecutive(a, k))
