from functools import reduce
from operator import mul
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    matches = get_matches(r'mul\(\d+,\d+\)')
    return sum(reduce(mul, ints(match)) for match in matches)

# Part 2 solution : 
def part_2():
    matches = get_matches(r"mul\(\d+,\d+\)|don't\(\)|do\(\)")
    enabled = True
    total = 0
    for match in matches:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        elif enabled:
            total += reduce(mul, ints(match))

    return total

def get_matches(r):
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_string(filename)

    return re.findall(r, data)


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
