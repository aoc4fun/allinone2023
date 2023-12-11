import helper.helper as aoc
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

sample_10="""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

sample_4 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

sample_8=""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

def prepare_data(data):
    return [[x for x in data2] for data2 in data.splitlines()]

def find_start(data):
    start=[]
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            if data[i][j] == "S":
                start=[i,j]
    next=None

    try:
        if data[start[0]][start[1]-1] in ["-","F","L"]:
            next=[start[0],start[1]-1]
    except:
        pass
    try:
        if data[start[0]][start[1]+1] in ["-","J","7"]:
            next=[start[0],start[1]+1]
    except:
        pass
    try:
        if data[start[0]-1][start[1]] in ["F","|","7"]:
            next=[start[0]-1,start[1]]
    except:
        pass
    try:
        if data[start[0]+1][start[1]] in ["J","|","L"]:
            next=[start[0]+1,start[1]]
    except:
        pass
    return (start,next)


def pipe_operator(op):
    if op=="|":
        return [(-1,0),(1,0)]
    if op=="-":
        return [(0,-1),(0,1)]
    if op=="7":
        return [(0,-1),(1,0)]
    if op=="J":
        return [(0,-1),(-1,0)]
    if op=="L":
        return [(0,1),(-1,0)]
    if op=="F":
        return [(1,0),(0,1)]

def next_step(data,position):
    current=position[1]
    old=position[0]
    direction=(old[0]-current[0],old[1]-current[1])
    op=pipe_operator(data[current[0]][current[1]])
    assert(direction in op)
    op.remove(direction)
    return (current,(current[0]+op[0][0],current[1]+op[0][1]))

def part_1(input_data):
    pipes = prepare_data(input_data)
    position=find_start(pipes)
    start=position[0]
    distance=1
    while True:
        if position[1][0] == start[0] and position[1][1] == start[1]:
            logger.debug(f"found start {position[1]}")
            break
        distance=distance+1
        position=next_step(pipes,position)

    return distance//2

def print_pipes(pipes):
    for i in pipes:
        for j in i:
            print(j,end="")
        print()

def part_2(input_data):
    pipes = prepare_data(input_data)
    position=find_start(pipes)
    start=position[0]
    distance=1
    # Mark the edge
    previous=False
    while True:
        if position[1][0] == start[0] and position[1][1] == start[1]:
            pipes[position[0][0]][position[0][1]] = "X"
            pipes[position[1][0]][position[1][1]] = "X"
            break
        current_position=position[0]
        next_position=position[1]
        position=next_step(pipes,position)
        direction = (next_position[0] - current_position[0])
        if direction == 1:
            pipes[current_position[0]][current_position[1]]="D"
            previous=True
        else:
            pipes[current_position[0]][current_position[1]] = "D" if previous else "X"
            previous=False
    counter=0
    for line in pipes:
        count=False
        for cur in line:
            if cur=="X":
                count=True
            if cur in ["J","-","F","|","-",".","L","7"] and count==True:
                counter=counter+1
            if cur=="D":
                count=False
    return counter


if __name__ == '__main__':
    assert (part_1(sample) == 8)
#    assert(part_2(sample_4)==4)
    assert(part_2(sample_8)==8)
    assert(part_2(sample_10)==10)

    aoc.retrieve_input(10, 2023)
    load_data = aoc.load_input(10, 2023)
    print(f"Day 10 part 1: {part_1(load_data)}")
    print(f"Day 10 part 2: {part_2(load_data)}")
