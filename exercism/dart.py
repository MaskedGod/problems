from math import sqrt


def score(x, y):
    points = 0
    # should've substracted center coords from dart but they are (0,0) so skip that step
    distance_to_center = sqrt(x**2 + y**2)
    print(distance_to_center)
    if 5 < distance_to_center <= 10:
        points = 1
    elif 1 < distance_to_center <= 5:
        points = 5
    elif distance_to_center <= 1:
        points = 10

    return points


print(score(5, 10))
print(score(0, 1))
print(score(3, 7))
print(score(11, 7))
print(score(-5, -10))
print(score(-5, 0))
print(score(-9, 9))
