
def read_from_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.split()

def main():
    a, b = [], []
    for i in read_from_file("test.txt"):
        a.append(i[0])
        b.append(i[1])
    a.sort()
    b.sort()
    print(sum(abs(int(i)-int(j)) for i, j in zip(a,b))) 

main()