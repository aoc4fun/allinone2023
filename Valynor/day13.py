import helper.helper as aoc
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

def prepare_data(data):
    return [mirror.splitlines() for mirror in data.split("\n\n")]

def find_diff(line1,line2):
    return len([i for i in range(0, len(line1)) if line1[i]!=line2[i]])

def find_horizontal_reflexion(data):
    for i in range(1, len(data)//2+1):
        isSymetric=len([j for j in range(0, i) if data[i-j-1]!=data[i+j]])==0
        if isSymetric:
            return i
        isSymetric=len([j for j in range(0, i) if data[len(data)-i-j-1]!=data[len(data)-i+j]])==0
        if isSymetric:
            return len(data)-i
    return 0

def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def find_vertical_reflexion(data):
    return find_horizontal_reflexion(trans(data))

def find_hypothetical_horizontal_reflexion(data):
    for i in range(1, len(data)//2+1):
        isSymetric=True
        diff=0
        for j in range(0, i):
            if data[i-j-1]!=data[i+j]:
                diff+=find_diff(data[i-j-1],data[i+j])
                isSymetric=False
        if isSymetric==False and diff==1:
            return i
        diff=0
        isSymetric = True
        for j in range(0, i):
            if data[len(data)-i-j-1]!=data[len(data)-i+j]:
                diff+=find_diff(data[len(data)-i-j-1],data[len(data)-i+j])
                isSymetric=False
        if isSymetric==False and diff==1:
            return len(data)-i
    return 0

def find_hypothetical_vertical_reflexion(data):
    return find_hypothetical_horizontal_reflexion(trans(data))

def part_1(input_data):
    mirror_list = prepare_data(input_data)
    horizontal=0
    vertical = 0
    for mirror in mirror_list:
        horizontal+=find_horizontal_reflexion(mirror)
        vertical+=find_vertical_reflexion(mirror)
    return horizontal*100+vertical

def part_2(input_data):
    mirror_list = prepare_data(input_data)
    horizontal=0
    vertical = 0
    for mirror in mirror_list:
        horizontal+=find_hypothetical_horizontal_reflexion(mirror)
        vertical+=find_hypothetical_vertical_reflexion(mirror)
    return horizontal*100+vertical


if __name__ == '__main__':
    assert (part_1(sample) == 405)
    assert (part_2(sample) == 400)

    aoc.retrieve_input(13, 2023)
    load_data = aoc.load_input(13, 2023)
    print(f"Day 13 part 1: {part_1(load_data)}")
    print(f"Day 13 part 2: {part_2(load_data)}")