# regular recursion fib
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(50))

# 1D memoization
term = [0 for i in range(10000000)]
def fibonacci_m(n):
    if n in [0, 1]:
        return n
    
    if term[n] != 0:
        return term[n]
    
    else:
        term[n] = fibonacci_m(n - 1) + fibonacci_m(n - 2)
        return term[n]
    
print(fibonacci_m(60))