def add(*args):
    ans = 0
    for i in args:
        ans += i
    print(ans)


add(3, 5, 6)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
