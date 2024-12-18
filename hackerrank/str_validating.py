# 1
if __name__ == "__main__":
    s = input()

res = False
for i in s:
    if i.isalnum():
        res = True
        break
print(res)

res = False
for j in s:
    if j.isalpha():
        res = True
        break
print(res)

res = False
for k in s:
    if k.isdigit():
        res = True
        break
print(res)

res = False
for l in s:
    if l.islower():
        res = True
        break
print(res)

res = False
for l in s:
    if l.isupper():
        res = True
        break
print(res)


# 2
if __name__ == "__main__":
    s = input()

    print(True in list(map(lambda n: n.isalnum(), s)))
    print(True in list(map(lambda n: n.isalpha(), s)))
    print(True in list(map(lambda n: n.isdigit(), s)))
    print(True in list(map(lambda n: n.islower(), s)))
    print(True in list(map(lambda n: n.isupper(), s)))

# 3
if __name__ == "__main__":
    s = input()

    print(True in list(map(lambda n: n.isalnum(), s)))
    print(True in list(map(lambda n: n.isalpha(), s)))
    print(True in list(map(lambda n: n.isdigit(), s)))
    print(True in list(map(lambda n: n.islower(), s)))
    print(True in list(map(lambda n: n.isupper(), s)))

# 4
if __name__ == "__main__":
    string = input()

    # Check for alphanumeric characters
    print(any(c.isalnum() for c in string))

    # Check for alphabetical characters
    print(any(c.isalpha() for c in string))

    # Check for digits
    print(any(c.isdigit() for c in string))

    # Check for lowercase characters
    print(any(c.islower() for c in string))

    # Check for uppercase characters
    print(any(c.isupper() for c in string))
