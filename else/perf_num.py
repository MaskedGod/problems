def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum([num for num in range(1, number) if number % num == 0])
    categories = {}
    categories["perfect"] = number == aliquot_sum
    categories["abundant"] = number < aliquot_sum
    categories["deficient"] = number > aliquot_sum

    for cat in categories.keys():
        if categories[cat]:
            return cat


print(classify(6))
print(classify(28))
print(classify(12))
print(classify(24))
print(classify(8))
print(classify(0))
