from datetime import datetime, timedelta


def add(moment):
    return moment + timedelta(seconds=1e9)


print(add(datetime(2011, 4, 25, 0, 0)))  # datetime(2043, 1, 1, 1, 46, 40))
