import helper.helper as aoc
import sys

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def prepare_data(data):
    clean_data = {}
    seeds = [int(seed) for seed in data.splitlines()[0].split(":")[1].split()]
    for line in data.splitlines()[1:]:
        if len(line) == 0:
            continue
        if "to" in line:
            current_map = line
            clean_data[current_map] = []
        else:
            clean_data[current_map].append([int(data) for data in line.split()])
    return seeds, clean_data


def return_soil(seed, transforms):
    for transform in transforms:
        if transform[1] <= int(seed) < transform[1] + transform[2]:
            return seed - transform[1] + transform[0]
    return seed


def part_1(input_data):
    seed, data = prepare_data(input_data)
    soils = []
    for i in seed:
        for name, transforms in data.items():
            i = return_soil(i, transforms)
        soils.append(i)
    return min(soils)


def splitter(vals, mapping):
    new_vals = []

    while len(vals) > 0:
        handled = False
        best_off = len(vals)

        for dst, src, size in mapping:
            if src <= vals[0] < src + size:
                off = vals[0] - src
                new_start = dst + off
                new_len = min(size - off, len(vals))
                new_vals.append(range(new_start, new_start + new_len))
                vals = vals[new_len:]
                handled = True
                break
            elif src < vals[0]:
                off = vals[0] - src
                best_off = min(best_off, off)

        if not handled:
            new_vals.append(vals[:best_off])
            vals = vals[best_off:]
    return new_vals


def return_soil_2(val_ranges, data):
    for mapping in data.values():
        new_ranges = []
        for r in val_ranges:
            new_ranges += splitter(r, mapping)
        val_ranges = new_ranges

    return min([val.start for val in val_ranges])


def part_2(input_data):
    seeds, data = prepare_data(input_data)

    min = sys.maxsize
    for a, b in zip(seeds[::2], seeds[1::2]):
        find = return_soil_2([range(a, a + b)], data)
        min = min if min < find else find

    return min


if __name__ == '__main__':
    assert (return_soil(53, [[50, 98, 2], [52, 50, 48]]) == 55)
    assert (return_soil(99, [[50, 98, 2], [52, 50, 48]]) == 51)
    assert (return_soil(98, [[50, 98, 2], [52, 50, 48]]) == 50)
    assert (return_soil(100, [[50, 98, 2], [52, 50, 48]]) == 100)
    assert (return_soil(79, [[50, 98, 2], [52, 50, 48]]) == 81)
    assert (part_1(sample) == 35)
    assert (part_2(sample) == 46)

    aoc.retrieve_input(5,2023)
    load_data = aoc.load_input(5,2023)
    print(f"Day 5 part 1: {part_1(load_data)}")
    print(f"Day 5 part 2: {part_2(load_data)}")
