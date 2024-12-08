nums = [x for x in range(1, 33)]
characters = [chr(char) for char in range(1040, 1040 + 32)]
print(nums)
print(characters)
dd = {k: v for k, v in zip(nums, characters)}
print(dd)


print("-----")
ddd = {k: chr(1040 + k - 1) for k in range(1, 33)}
print(ddd)


char = ord("А")

dddd = {k: chr(char + k - 1) for k in range(1, 33)}
print(dddd)
