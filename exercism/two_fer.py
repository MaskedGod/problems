def two_fer(name="you"):
    phrase = f"One for {name}, one for me."
    return phrase


print(two_fer())  # "One for you, one for me.")
print(two_fer("Alice"))  # "One for Alice, one for me.")
print(two_fer("Bob"))  # "One for Bob, one for me.")
