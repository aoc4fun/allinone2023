import helper.helper as aoc
import math
import logging

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
        left, right = node_data.replace("(", "").replace(")", "").split(", ")
        list_nodes[node_name] = [left, right]
    return orders, list_nodes


def part_1(input_data):
    orders, nodes = prepare_data(input_data)
    current_node = "AAA"
    length = 0
    while current_node != "ZZZ":
        logger.debug(f'Current node: {current_node} with order {orders}')
        current_node = nodes[current_node][orders[length % len(orders)] == "R"]
        length += 1
    return length


def find_start_node(nodes):
    return [node for node, data in nodes.items() if node.endswith("A")]


def find_length(current_path, orders, nodes):
    length = 0
    while not current_path.endswith("Z"):
        current_path=nodes[current_path][orders[length % len(orders)] == "R"]
        length += 1
    return length


def part_2(input_data):
    orders, nodes = prepare_data(input_data)
    currents_length = [find_length(current_path, orders, nodes) for current_path in find_start_node(nodes)]
    logger.debug(f"Length: {currents_length}")
    return math.lcm(*currents_length)


if __name__ == '__main__':
    assert (part_1(sample) == 2)
    assert (part_1(sample2) == 6)
    assert (part_2(sample3) == 6)

    aoc.retrieve_input(8, 2023)
    load_data = aoc.load_input(8, 2023)
    print(f"Day 8 part 1: {part_1(load_data)}")
    print(f"Day 8 part 2: {part_2(load_data)}")
