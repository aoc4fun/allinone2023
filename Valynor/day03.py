import helper.helper as aoc
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def prepare_data(data):
    return [list(line) for line in data.splitlines()]

def is_symbol(symbol):
    if not symbol.isdigit() and symbol!=".":
        return True

def is_gear(symbol):
    return (symbol=="*")

def find_symbol(data,pos_char,linenumber):
    for i in range(pos_char-1,pos_char+2):
        for j in range(linenumber-1,linenumber+2):
            try:
                if is_symbol(data[j][i]):
                   return True
            except:
                pass
    return False

def scanline(data,linenumber):
    numbers=[]
    in_digit=False
    near=False
    for pos_char in range(0,len(data[linenumber])):
        if data[linenumber][pos_char].isdigit():
            if in_digit:
                in_digit=in_digit+data[linenumber][pos_char]
            else:
                in_digit=data[linenumber][pos_char]
            near=near or find_symbol(data,pos_char,linenumber)
        else:
            if in_digit and near:
                numbers.append(int(f"{in_digit}"))
                logger.info(f"Found number: {in_digit} near a symbol")
                in_digit=False
                near=False
    if in_digit and near:
        numbers.append(int(f"{in_digit}"))
        logger.info(f"Found number: {in_digit} near a symbol")
    return sum(numbers)

def part_1(input_data):
    data=prepare_data(input_data)
    result = []
    for line in range(0,len(data)):
        result.append(scanline(data,line))
    return sum(result)


def part_2(input_data):
    prepared_data = prepare_data(input_data)
    return part_1(prepared_data)


if __name__ == '__main__':
    print(part_1(sample))
    assert (part_1(sample) == 4361)
    assert (part_2(sample) == 467835)

    aoc.retrieve_input(3,2023)
    load_data = aoc.load_input(3,2023)
    print(f"Day 3 part 1: {part_1(load_data)}")
#    print(f"Day 1 part 2: {part_2(load_data)}")

