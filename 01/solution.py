import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = [ints(line) for line in open(filename, "r")]
    left = sorted([line[0] for line in data])
    right = sorted([line[1] for line in data])

    difs = [max(x, y) - min(x, y) for (x, y) in zip(left, right)]
    return sum(difs)

# Part 2 solution : 
def part_2():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = [ints(line) for line in open(filename, "r")]
    left = sorted([line[0] for line in data])
    right = sorted([line[1] for line in data])

    return sum(item * right.count(item) for item in left)


if __name__ == "__main__":
    s = time.time()
    p1 = part_1()
    e = time.time()
    t1 = e - s

    s = time.time()
    p2 = part_2()
    e = time.time()
    t2 = e - s
    pretty_print(p1, p2, t1, t2)
