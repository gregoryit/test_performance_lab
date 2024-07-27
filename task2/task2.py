import sys


circle_file, dot_file = sys.argv[1:]

with open(circle_file) as f:
    x0, y0 = map(int, f.readline().split())
    r = int(f.readline())

with open(dot_file) as f:
    dots = [map(float, line.split()) for line in f]
    for x, y in dots:
        result = (x - x0) ** 2 + (y - y0) ** 2 - r ** 2
        if result > 0:
            print(2)
        elif result < 0:
            print(1)
        else:
            print(0)

