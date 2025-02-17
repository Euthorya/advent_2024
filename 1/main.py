
def read_from_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.split()

def main():
    a, b = [], []
    for i in read_from_file("test.txt"):
        a.append(int(i[0]))
        b.append(int(i[1]))
    a.sort()
    b.sort()
    print(sum(abs(i-j) for i, j in zip(a,b)))

    m = {}
    for i in b:
        m[i] = m.get(i, 0) + 1
    print(sum(i * m[i] for i in a if i in m))

main()