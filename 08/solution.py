from collections import defaultdict
from functools import reduce

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    data, H, W = get_data()
    d = get_antenna_dict(data)
    antinodes = get_antinodes(d, H, W)

    return len(antinodes)

# Part 2 solution : 
def part_2():
    data, H, W = get_data()
    d = get_antenna_dict(data)
    antinodes = get_antinodes(d, H, W, 1000)

    # return unique antinodes + all original antennas
    return len(antinodes | reduce(lambda a, b: a | b, (values for key, values in d.items())))

def get_antenna_dict(data):
    d = defaultdict(set)
    for y, line in enumerate(data):
        for x, elem in enumerate(line):
            if elem != ".":
                d[elem].add((y, x))
    return d

def get_data():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep="", f=str)
    H, W = len(data), len(data[0])

    return data, H, W


def get_antinodes(d, H, W, iterations=1):
    antinodes = set()
    for key, antennas in d.items():
        for y1, x1 in antennas:
            for y2, x2 in antennas:
                if x1 == x2 and y1 == y2:
                    continue
                for i in range(iterations):
                    dx = (x2 - x1) * (i + 1)
                    dy = (y2 - y1) * (i + 1)
                    new_y, new_x = y1 - dy, x1 - dx
                    if new_y < 0 or new_y >= H or new_x < 0 or new_x >= W:
                        break

                    antinodes.add((new_y, new_x))
    return antinodes

if __name__ == "__main__":
    pretty_print_parts(part_1, part_2)
