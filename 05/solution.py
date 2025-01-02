import math
from collections import deque, defaultdict
from functools import reduce
from operator import mul
import itertools
import numpy as np
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    instructions, d = get_data()
    ok_lines, _ = get_ok_not_ok_lines(instructions, d)

    return sum(line[int(len(line)/2)] for line in ok_lines)


# Part 2 solution : 
def part_2():
    instructions, d = get_data()
    _, not_ok_lines = get_ok_not_ok_lines(instructions, d)

    fixed = [fix_instructions(d, line, []) for line in not_ok_lines]
    return sum(line[int(len(line)/2)] for line in fixed)

def get_ok_not_ok_lines(instructions, d):
    ok_lines = []
    not_ok_lines = []
    for line in instructions:
        trimmed_dict = {key: [x for x in value if x in line] for key, value in d.items() if key in line}
        SEEN = set()
        for elem in line:
            if elem in trimmed_dict.keys() and not all(x in SEEN for x in trimmed_dict[elem]):
                not_ok_lines.append(line)
                break
            SEEN.add(elem)
        else:
            ok_lines.append(line)

    return ok_lines, not_ok_lines


def get_data():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines(filename, f=str)
    split = data.index("")
    first = [tuple(ints(line)) for line in data[:split]]
    second = [[int(c) for c in line.split(",")] for line in data[split+1:]]

    d = build_dict(first)

    return second, d

def fix_instructions(d, line, current):
    line = [x for x in line if x not in current]
    if len(line) == 1:
        current.append(line[0])
        return current

    trimmed_dict = {key: [x for x in value if x in line] for key, value in d.items() if key in line}
    root = [x for x in line if x not in trimmed_dict.keys() or len(trimmed_dict[x]) == 0][0]
    current.append(root)
    return fix_instructions(d, line, current)


def build_dict(data):
    d = defaultdict(list)
    for line in data:
        d[line[1]].append(line[0])

    return d



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
