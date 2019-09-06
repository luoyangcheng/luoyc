import itertools

mylist = ("".join(x) for x in itertools.product(
    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    repeat=16))
while True:
    print(next(mylist))
