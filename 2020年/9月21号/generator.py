# 迭代器

gen = (x * x for x in range(1, 11))

print(gen)


def f(x):
    return x * x


l = map(f, [1, 2, 3, 4, 5, 6])
print(list(l))

print(list(map(str, [1, 2, 3, 4, 5, 6])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisable(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it =  filter(_not_divisable(n), it)