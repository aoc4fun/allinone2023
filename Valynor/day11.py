import helper.helper as aoc
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def prepare_data(data):
    return [[x for x in data2] for data2 in data.splitlines()]


def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def print_galaxy(data):
    for i in data:
        print("".join(i))
    print("")


def find_horizontal(data):
    return [i for i in range(0, len(data)) if all([x == "." for x in data[i]])]


def find_vertical(data):
    data = trans(data)
    return find_horizontal(data)


def find_expansion_galaxy(data):
    horizontal = find_horizontal(data)
    vertical = find_vertical(data)
    return horizontal, vertical


def find_galaxy(data):
    result = []
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == "#":
                result.append([i, j])
    return result


def find_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def find_distance_expension(galaxy1, galaxy2, expension, expension_size):
    expension_add = 0
    for i in expension[0]:
        if i >= (min(galaxy1[0], galaxy2[0])) and i <= (max(galaxy1[0], galaxy2[0])):
            expension_add += 1
    for i in expension[1]:
        if i >= (min(galaxy1[1], galaxy2[1])) and i <= (max(galaxy1[1], galaxy2[1])):
            expension_add += 1
    return find_distance(galaxy1, galaxy2) + expension_add * (expension_size - 1)


def find_all_distance_generic(galaxy, expension, expension_size):
    result = []
    for i in range(0, len(galaxy)):
        for j in range(i + 1, len(galaxy)):
            result.append(find_distance_expension(galaxy[i], galaxy[j], expension, expension_size))
    return sum(result)


def part_1(input_data):
    univers = prepare_data(input_data)
    expension = find_expansion_galaxy(univers)
    galaxies = find_galaxy(univers)
    result = find_all_distance_generic(galaxies, expension, 2)
    return result


def part_2(input_data, expension_size):
    univers = prepare_data(input_data)
    expension = find_expansion_galaxy(univers)
    galaxies = find_galaxy(univers)
    result = find_all_distance_generic(galaxies, expension, expension_size)
    return result


if __name__ == '__main__':
    assert (part_1(sample) == 374)
    assert (part_2(sample, expension_size=2) == 374)
    assert (part_2(sample, expension_size=10) == 1030)
    assert (part_2(sample, expension_size=100) == 8410)

    aoc.retrieve_input(11, 2023)
    load_data = aoc.load_input(11, 2023)
    print(f"Day 11 part 1: {part_1(load_data)}")
    print(f"Day 11 part 2: {part_2(load_data, 1000000)}")
