import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = [int(c) for c in read_string(filename).strip()]

    mem = [str(i//2) if i % 2 == 0 else "." for i, segment_length in enumerate(data) for _ in range(segment_length)]

    left, right = 0, len(mem) -1
    while right > left:
        if mem[right] == ".":
            right -= 1
        elif mem[left] == ".":
            mem[left] = mem[right]
            mem[right] = "."
            right -= 1
            left += 1
        else:
            left += 1

    return sum(int(x) * i if x != "." else 0 for i, x in enumerate(mem))

# Part 2 solution : 
def part_2():
    filename = sys.argv[1] if len(sys.argv) == 2 else "input.txt"
    data = [int(c) for c in read_string(filename).strip()]


    # Builds lists with all spaces and files and their respective indexes as well as lengths
    files, spaces = [], []
    mem_addr = 0
    for i, segment_length in enumerate(data):
        if i % 2 == 0:
            files.append((mem_addr, segment_length, i//2))
        else:
            spaces.append((mem_addr, segment_length))
        mem_addr += segment_length

    # 
    for i in range(len(files)-1, 0, -1):
        space_index = 0
        for space_index in range(len(spaces)):
            space_addr, space_length = spaces[space_index]
            file_addr, file_length, file_index = files[i]

            # avoid swapping to 'later' addr
            if space_addr > file_addr:
                break

            # If room for file at earlier addr
            if file_length <= space_length:
                spaces.append((file_addr, file_length))
                files[i] = (space_addr, file_length, file_index)
                if file_length == space_length:
                    del spaces[space_index]
                else:
                    spaces[space_index] = (space_addr + file_length, space_length - file_length)


    return sum((addr + i) * value for addr, length, value in files for i in range(length))

if __name__ == "__main__":
    pretty_print_parts(part_1, part_2)
