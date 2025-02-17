from functools import reduce

def read_from_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

def reducer(asc):
    def wrapper(x, y):
        if x is None or y is None:
            return None
        return y if 0 < abs(x-y) < 4 and (x < y) is asc else None
    return wrapper

def reducer_tolerant(asc, factor):
    f = factor
    def wrapper(x, y):
        nonlocal f
        if x is None or y is None:
            return None
        if 0 < abs(x-y) < 4 and (x < y) == asc:
            return y
        elif f > 0:
            f -= 1
            return x
        return None
    return wrapper

def sign(n):
    s = 0
    for i in range(3):
        if (n[i] < n[i+1]):
            s += 1
        else:
            s -= 1
    return s > 0

def main():
    result = 0
    for i in read_from_file("test.txt"):
        numbers = list(map(int, i.split()))
        if reduce(reducer(numbers[0] < numbers[1]), numbers):
            result += 1
    print(result)

    result = 0
    for i in read_from_file("test.txt"):
        numbers = list(map(int, i.split()))
        if any(reduce(reducer_tolerant(sign(numbers[::i]), 1), numbers[::i]) for i in [1, -1]):
            result += 1
    print(result)



main()