from copy import deepcopy
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

SPIN_DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Part 1 solution : 
def part_1():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep="", f=str)

    current_pos = get_start_pos(data)
    current_dir = 3
    

    visited = set(current_pos)
    while True:
        # GEt the direction and the new y,x
        dy, dx = SPIN_DIRS[current_dir % len(SPIN_DIRS)]
        current_y, current_x = current_pos
        new_y, new_x = current_y + dy, current_x + dx

        if is_out_of_bounds(data, new_y, new_x):
            break
        
        if data[new_y][new_x] == "#":
            current_dir += 1
            continue

        current_pos = (new_y, new_x)
        if current_pos not in visited:
            visited.add(current_pos)

    return len(visited)

def get_start_pos(data):
    for y, line in enumerate(data):
        for x, elem in enumerate(line):
            if elem == "^":
                return (y, x)

def is_out_of_bounds(data, y, x):
    return y < 0 or y >= len(data) or x < 0 or x >= len(data[0])



# Part 2 solution : 
def part_2():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep="", f=str)

    start_pos = get_start_pos(data)
    loops = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            current_pos = start_pos
            current_dir = 3
    
            visited = set((current_pos, current_dir))
            if data[i][j] in ["^", "#"]:
                continue

            while True:
                # GEt the direction and the new y,x
                dy, dx = SPIN_DIRS[current_dir]
                current_y, current_x = current_pos
                new_y, new_x = current_y + dy, current_x + dx

                if is_out_of_bounds(data, new_y, new_x):
                    break
                
                if data[new_y][new_x] == "#" or (new_y, new_x) == (i, j):
                    current_dir = (current_dir + 1) % len(SPIN_DIRS)
                    continue

                current_pos = (new_y, new_x)
                if (current_pos, current_dir) not in visited:
                    visited.add((current_pos, current_dir))
                else:
                    res += 1
                    break

    return loops


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
