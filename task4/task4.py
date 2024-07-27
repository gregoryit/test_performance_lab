import sys

numbers_file = sys.argv[1]

with open(numbers_file) as f:
    numbers = list(map(int, f.readlines()))

numbers.sort()
median = numbers[len(numbers) // 2]
steps = sum(abs(s - median) for s in numbers)
print(steps)
