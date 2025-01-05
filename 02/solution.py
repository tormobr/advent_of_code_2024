import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep=" ", f=int)
    safe_lines = [safe(line) or safe(line, is_ascending = False) for line in data]

    return sum(safe_lines)

# Part 2 solution : 
def part_2():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = read_lines_sep(filename, sep=" ", f=int)
    safe_lines = [safe(line, allow_single_bad = True) or safe(line, allow_single_bad = True, is_ascending = False) for line in data]

    return sum(safe_lines)

def safe(arr, allow_single_bad = False, is_ascending = True):
    for i in range(len(arr) - 1):
        if not safe_elements(arr[i], arr[i+1], is_ascending):
            if not allow_single_bad:
                return False
            else:
                left = arr[:i] + arr[i+1:] # Remove first in pair
                right = arr[:i+1] + arr[i+2:] # Remove second in pair
                return safe(left, is_ascending = is_ascending) or safe(right, is_ascending = is_ascending)

    return True


def safe_elements(a, b, is_ascending):
    if not is_ascending:
        a, b = b, a
    return a < b and b - a <= 3


if __name__ == "__main__":
    pretty_print_parts(part_1, part_2)
