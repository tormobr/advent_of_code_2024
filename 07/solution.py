from operator import mul, add, sub
import itertools

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    return solve([add, mul])

# Part 2 solution : 
def part_2():
    return solve([add, mul, lambda a, b: int(str(a) + str(b))])

def solve(operators):
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    res = 0
    for line in open(filename, "r"):
        left, right = line.split(":")
        test = ints(left)[0]
        nums = ints(right)
        ops_cobs = itertools.product(operators, repeat=len(nums)-1)
        for operations in ops_cobs:
            total = 0
            total = nums[0]
            for i in range(len(nums) - 1):
                total = operations[i](total, nums[i+1])
            if total == test:
                res += test
                break
    return res


if __name__ == "__main__":
    pretty_print_parts(part_1, part_2)
