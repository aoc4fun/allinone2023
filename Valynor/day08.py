import helper.helper as aoc
import sys

import logging
from functools import reduce
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

sample2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

sample3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def prepare_data(data):
    orders, nodes = data.split("\n\n")
    list_nodes = {}
    for node in nodes.splitlines():
        node_name, node_data = node.split(" = ")
        node_data = node_data.replace("(", "").replace(")", "").split(", ")
        node_data = [node_data[0], node_data[1]]
        list_nodes[node_name.strip()]= node_data
    return orders, list_nodes

def part_1(input_data):
    orders, nodes = prepare_data(input_data)
    currentNode="AAA"
    length=0
    while True:
        for order in orders:
            length += 1
            logger.debug(f'Current node: {currentNode} with order {order}')
            currentNode=nodes[currentNode][order=="R"]
        if currentNode=="ZZZ":
            return length

def move(currentNode, nodes, order):
    return nodes[currentNode][(order=="R")]

def find_start_node(nodes):
    return [node for node, data in nodes.items() if node.endswith("A")]

def find_lenght(start,orders,nodes):
    current_path=start
    length=0
    while True:
        for order in orders:
            length += 1
            current_path=move(current_path, nodes, order)
            if current_path.endswith("Z"):
                return length
    return None

from math import gcd

def part_2(input_data):
    orders, nodes = prepare_data(input_data)
    currents_length=[find_lenght(current_path,orders,nodes) for current_path in find_start_node(nodes)]
    logger.debug(f"Length: {currents_length}")
    lcm = 1
    for i in currents_length:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

if __name__ == '__main__':
    assert (part_1(sample) == 2)
    assert (part_1(sample2) == 6)
    assert (part_2(sample3) == 6)

    aoc.retrieve_input(8,2023)
    load_data = aoc.load_input(8,2023)
    print(f"Day 5 part 1: {part_1(load_data)}")
    print(f"Day 5 part 2: {part_2(load_data)}")
