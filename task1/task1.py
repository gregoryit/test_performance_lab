import sys
from math import lcm

n, m = map(int, sys.argv[1:])

l = list(range(1, n + 1))
nok = lcm(n, m - 1)
k = nok // n
l *= k

print(*l[::m-1], sep='')
