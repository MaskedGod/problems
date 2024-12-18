def tribonacci(signature, n):
    a, b, c = signature
    res = []
    if n > 0:
        while len(res) < n:
            res.append(a)
            a, b, c = b, c, a + b + c

    return res


def tribonacci2(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


print(tribonacci([1, 1, 1], 10))
