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
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines(filename, f=int)
    data = read_string(filename)
    data = read_sep(filename, sep=",", f=int)
    data = read_lines_sep(filename, sep=",", f=str)

    print_arr(data)

    return None

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print_parts(part_1, part_2)
