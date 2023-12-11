import helper.helper as aoc
import sys

import logging
from functools import reduce
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """Time:      7  15   30
Distance:  9  40  200"""


def prepare_data(data):
    result={}
    data1=[int(x) for x in data.splitlines()[0].split(":")[1].split()]
    data2=[int(x) for x in data.splitlines()[1].split(":")[1].split()]
    for i in range(0,len(data1)):
        result[i]={"time":data1[i],"distance":data2[i]}
    return result

def prepare_data2(data):
    data1=int(data.splitlines()[0].split(":")[1].replace(" ",""))
    data2=int(data.splitlines()[1].split(":")[1].replace(" ",""))
    return {"time":data1,"distance":data2}

def find_winner_move(time,distance):
    win_game=0
    speed=0
    while speed<time:
        if (time-speed)*speed>distance:
            win_game+=1
        speed+=1
    return win_game

def part_1(input_data):
    data = prepare_data(input_data)
    return reduce(lambda x, y: x*y,[find_winner_move(items["time"],items["distance"]) for items in data.values()])


def part_2(input_data):
    data = prepare_data2(input_data)
    return find_winner_move(data["time"],data["distance"])



if __name__ == '__main__':
    print(prepare_data(sample))
    print(find_winner_move(7,9))
    print(find_winner_move(15,40))
    print(find_winner_move(30,200))
    assert (part_1(sample) == 288)
    assert (part_2(sample) == 71503)

    aoc.retrieve_input(6,2023)
    load_data = aoc.load_input(6,2023)
    print(f"Day 6 part 1: {part_1(load_data)}")
    print(f"Day 6 part 2: {part_2(load_data)}")
