import PIL

import helper.helper as aoc
import math
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

def prepare_data(data):
    return data.split(",")

def hash(string):
    result=0
    for ch in string:
        result=((result+ord(ch))*17)%256
    return result

def part_1(input_data):
    data=prepare_data(input_data)
    return sum([hash(string.strip()) for string in data])

def search_ops(op,box):
    for i in range(len(box)):
        if box[i][0]==op:
            return i
    return -1

def fill_box(data):
    box=[[] for _ in range(256)]
    for instruction in data:
        ops=instruction.split("-")[0].split("=")
        op=ops[0]
        box_number = hash(op)
        search = search_ops(op, box[box_number])
        if len(ops)==1:
            if search!=-1:
                box[box_number].pop(search)
        else:
            if search==-1:
                box[box_number].append([op,ops[1]])
            else:
                box[box_number][search]=[op,ops[1]]
    return box

def compute_focus_power(box):
    result=0
    for b in range(len(box)):
        for f in range(len(box[b])):
            result+=((b+1)*(f+1)*int(box[b][f][1]))
    return result
def part_2(input_data):
    data = prepare_data(input_data)
    box=fill_box(data)
    return compute_focus_power(box)

if __name__ == '__main__':
    assert(hash("HASH")==52)
    assert (hash("rn") == 0)
    assert (part_1(sample) == 1320)
    assert (part_2(sample) == 145)

    aoc.retrieve_input(15, 2023)
    load_data = aoc.load_input(15, 2023)
    print(f"Day 14 part 1: {part_1(load_data)}")
    print(f"Day 14 part 2: {part_2(load_data)}")
