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

DIRECTIONS = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0)
}

# Part 1 solution : 
def part_1():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep="", f=int)

    return sum(DFS(y, x, -1, data, set(), set()) for y, line in enumerate(data) for x, elem in enumerate(line) if elem == 0)

# Part 2 solution : 
def part_2():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep="", f=int)

    return sum(DFS(y, x, -1, data, set(), set(), get_paths=True) for y, line in enumerate(data) for x, elem in enumerate(line) if elem == 0)

def DFS(y, x, prev_elem, data, seen, seen_targets, get_paths=False):
    if (y, x) in seen or y < 0 or x < 0 or y >= len(data) or x >= len(data[0]):
        return 0

    seen.add((y, x))
    elem = data[y][x]
    if elem != prev_elem + 1:
        return 0

    if elem == 9 and ((y, x) not in seen_targets or get_paths):
        seen_targets.add((y, x))
        return 1

    ret = 0
    for dy, dx in DIRECTIONS.values():
        new_y, new_x = y + dy, x + dx
        ret += DFS(new_y, new_x, elem, data, seen.copy(), seen_targets, get_paths)

    return ret

if __name__ == "__main__":
    pretty_print_parts(part_1, part_2)
