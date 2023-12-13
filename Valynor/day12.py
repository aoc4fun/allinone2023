import helper.helper as aoc
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def prepare_data(data):
    return data.splitlines()

cache = {}
def count_ways(s, nums):
    if (s, tuple(nums)) in cache:
        return cache[(s, tuple(nums))]

    if len(nums) == 0:
        return 1 if "#" not in s else 0

    size = nums[0]
    total = 0

    for i in range(len(s)):
        if (
            i + size <= len(s)
            and all(c != "." for c in s[i : i + size])
            and (i == 0 or s[i - 1] != "#")
            and (i + size == len(s) or s[i + size] != "#")
        ):
            total += count_ways(s[i + size + 1 :], nums[1:])

        if s[i] == "#":
            break

    cache[(s, tuple(nums))] = total

    return total


def get_total(lines,times):
    total = 0

    for line in lines:
        row, nums = line.split()
        row = "?".join([row] * times)
        nums = [int(n) for n in nums.split(",")] * times
        total += count_ways(row, nums)
    return total

def part_1(input_data):
    lines = prepare_data(input_data)
    return get_total(lines,1)

def part_2(input_data):
    lines = prepare_data(input_data)
    return get_total(lines,5)

if __name__ == '__main__':
    assert (part_1(sample) == 21)
    assert (part_2(sample) == 525152)

    aoc.retrieve_input(12, 2023)
    load_data = aoc.load_input(12, 2023)
    print(f"Day 12 part 1: {part_1(load_data)}")
    print(f"Day 12 part 2: {part_2(load_data)}")
