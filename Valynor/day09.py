import helper.helper as aoc
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def prepare_data(data):
    return [[int(x) for x in data2.split()] for data2 in data.splitlines()]

def is_zero(data):
    return all([x == 0 for x in data])

def next_step(data):
    result= []
    for i in range(0, len(data)-1):
        result.append(data[i+1] - data[i] )
    return result

def all_in_one(data,position=-1):
    pyramide=[data]
    while not is_zero(data):
        data = next_step(data)
        pyramide.append(data)
    for i in range(len(pyramide)-1,0,-1):
        pyramide[i-1][position]=pyramide[i-1][position]+(-2*position-1)*pyramide[i][position]
    return pyramide[0][position]


def part_1(input_data):
    data = prepare_data(input_data)
    result=[]
    for i in data:
        result.append(all_in_one(i))
    return sum(result)


def part_2(input_data):
    data = prepare_data(input_data)
    result=[]
    for i in data:
        result.append(all_in_one(i,0))
    return sum(result)


if __name__ == '__main__':
    assert (part_1(sample) == 114)
    assert (part_2(sample) == 2)

    aoc.retrieve_input(9, 2023)
    load_data = aoc.load_input(9, 2023)
    print(f"Day 5 part 1: {part_1(load_data)}")
    print(f"Day 5 part 2: {part_2(load_data)}")
