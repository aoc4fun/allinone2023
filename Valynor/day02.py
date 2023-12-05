import helper.helper as aoc
import logging
from functools import reduce

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

part_1_guess={"red":12,"blue":14,"green":13}

def parse_line(input_line):
    game, data = input_line.split(":")
    game_number = int(game.split(" ")[1])
    data = data.split(";")
    result=[]
    for grab in data:
        cubes = grab.split(",")
        cubegrab={}
        for cube in cubes:
            _, number, color = cube.split(" ")
            cubegrab[color]=int(number)
        result.append(cubegrab)
    return game_number, result

def check_game(draws, guess):
    for draw in draws:
        for color, number in draw.items():
            if guess[color] < number:
                return False
    return True


def part_1(input_data):
    result = []
    for line in input_data:
        game, draws = parse_line(line)
        if check_game(draws, part_1_guess):
            result.append(game)
    return sum(result)

def power(draws):
    min = {"green":0,"blue":0,"red":0}
    for draw in draws:
        for color, number in draw.items():
            if min[color] < number:
                min[color]=number
    return reduce(lambda x,y: x*y, min.values())

def part_2(input_data):
    result = []
    for line in input_data:
        game, draws = parse_line(line)
        result.append(power(draws))
    return sum(result)

if __name__ == '__main__':
    assert (parse_line(sample.splitlines()[0]) == (1, [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]))
    assert(part_1(sample.splitlines())==8)
    assert (power(parse_line(sample.splitlines()[0])[1]) == 48)
    assert (part_2(sample.splitlines()) == 2286)

    aoc.retrieve_input(2,2023)
    load_data = aoc.load_input(2,2023).splitlines()
    print(f"Day 2 part 1: {part_1(load_data)}")
    print(f"Day 2 part 2: {part_2(load_data)}")

