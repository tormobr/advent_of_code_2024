import numpy as np

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep="", f=str)

    return sum(search_xmas(data, x, y) if elem == "X" else 0 for y, line in enumerate(data) for x, elem in enumerate(line))

# Part 2 solution : 
def part_2():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep="", f=str)

    return sum(search_mas(data, x, y) if elem == "A" else 0 for y, line in enumerate(data) for x, elem in enumerate(line))

def search_mas(data, x, y):
    arr = np.array(data)

    left_downward_diagonal = (y-1, x-1, (1, 1))
    right_downward_diagonal = (y-1, x+1, (-1, 1))

    left_upward_diagonal = (y+1, x-1, (1, -1))
    right_upward_diagonal = (y+1, x+1, (-1, -1))

    dirs = [left_downward_diagonal, right_downward_diagonal, left_upward_diagonal, right_upward_diagonal]

    word = "MAS"
    c = 0
    for start_y, start_x, (dx, dy) in dirs:
        for i in range(len(word)):
            new_x, new_y = start_x + dx * i, start_y + dy * i
            if new_x < 0 or new_x >= len(arr[0]) or new_y < 0 or new_y >= len(arr) or arr[new_y, new_x] != word[i]:
                break;
        else:
            c += 1

    return 1 if c == 2 else 0

def search_xmas(data, x, y):
    arr = np.array(data)
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    word = "XMAS"
    c = 0
    for dx, dy in DIRS:
        for i in range(len(word)):
            new_x, new_y = x + dx * i,  y + dy * i
            if new_x < 0 or new_x >= len(arr[0]) or new_y < 0 or new_y >= len(arr) or arr[new_y, new_x] != word[i]:
                break;
        else:
            c += 1

    return c


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
