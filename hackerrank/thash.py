if __name__ == "__main__":
    N = int(input())
    nums = input().split()
    t = tuple(int(n) for n in nums)

    print(hash(t))
