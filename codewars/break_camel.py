import re


s = "breakCamelCase"


def solution(s):
    return " ".join(re.split(pattern="(?=[A-Z])", string=s))


def solution2(s):
    return re.sub("(?=[A-Z])", " ", s)


print(solution2(s))
