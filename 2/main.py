from functools import reduce

def read_from_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

def reducer(asc):
    def wrapper(x, y):
        if x is None or y is None:
            return None
        x, y = int(x), int(y)
        return y if 0 < abs(x-y) < 4 and (x < y) == asc else None
    return wrapper

def main():
    result = 0
    valid_lines = []
    for i in read_from_file("test.txt"):
        numbers = i.split()
        valid = reduce(reducer(int(numbers[0]) < int(numbers[1])), numbers)
        if valid:
            result += 1
            valid_lines.append(i)
    print(result)


main()