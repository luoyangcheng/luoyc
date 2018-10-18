#
def login():
    i = [0, 1, 2]
    j = [0, 1, 3]
    for a, b in zip(i, j):
        assert a == b
