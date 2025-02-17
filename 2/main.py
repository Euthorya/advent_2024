from functools import reduce

def read_from_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line


def reducer(asc):
    #asc = asc
    def wrapper(x, y):
        if x is None or y is None:
            return None
        x, y = int(x), int(y)
        return y if 0 < abs(x-y) < 4 and (x < y) == asc else None
    return wrapper
        





def main():
    a = [i for i in read_from_file("test.txt")]
    result = 0
    valid_lines = []
    for i in a:
        # numbers = i.split()
        # valid = reduce(reducer(numbers[0] < numbers[1]), numbers)
        # if valid:
        #     result += 1
        #     valid_lines.append(i)
        numbers = i.split()
        asc = numbers[0] < numbers[1]
        valid = True
        for j in range(len(numbers)-1):
            if not (0< abs(int(numbers[j+1]) - int(numbers[j])) < 4) or (int(numbers[j]) < int(numbers[j+1]))!= asc:
                valid = False
                break
        if valid:
            result += 1
                

    print(result)


main()