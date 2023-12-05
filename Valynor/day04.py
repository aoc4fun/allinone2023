import helper.helper as aoc
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def prepare_data(data):
    clean_data = []
    for line in data.splitlines():
        winner, hand = line.split(":")[1].split("|")
        clean_data.append([list(winner.split()), list(hand.split())])
    return clean_data


def part_1(input_data):
    data = prepare_data(input_data)
    return sum([int(pow(2, len(set(i).intersection(j)) - 1)) for i, j in data])


from collections import defaultdict


def part_2(input_data):
    data = prepare_data(input_data)
    copy = defaultdict(int)
    for cardnumber in range(1, len(data) + 1):
        winnercard = len(set(data[cardnumber - 1][0]).intersection(data[cardnumber - 1][1]))
        copy[cardnumber] += 1
        for i in list(range(cardnumber + 1, cardnumber + winnercard + 1)):
            copy[i] += copy[cardnumber]
    return sum(copy.values())


if __name__ == '__main__':
    assert (part_1(sample) == 13)
    assert (part_2(sample) == 30)

    aoc.retrieve_input(4,2023)
    load_data = aoc.load_input(4,2023)
    print(f"Day 4 part 1: {part_1(load_data)}")
    print(f"Day 4 part 2: {part_2(load_data)}")
