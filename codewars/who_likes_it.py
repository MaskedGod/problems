def likes(names: list) -> str:
    length = len(names)
    if length == 0:
        return 'no one likes this'
    if length == 1:
        return f'{names[0]} likes this'
    elif length == 2:
        return f'{names[0]} and {names[1]} like this'
    elif length == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this' 
    else:
        return f'{names[0]}, {names[1]} and {length - 2} others like this'



print(likes([]))
print(likes(['Peter']))
print(likes(['Peter', 'Jacob']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Alex', 'Jacob', 'Mark', 'Max']))