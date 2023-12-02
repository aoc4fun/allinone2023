import os
import requests
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
adventcookie = os.getenv('adventcookie')
url = 'https://adventofcode.com/2023/day/1/input'
file_path = 'input_1.txt'


def retrieve_input():
    if not os.path.exists(file_path):
        response = requests.get(url,
                                headers={'cookie': f'session={adventcookie}', 'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            logger.info(f"File downloaded and saved as {file_path}")
        else:
            logger.error(f"Failed to download the file. Status code: {response.status_code}")
    else:
        logger.info(f"The file [{file_path}] already exists.")


sample = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

sample2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

sample3 = """twone
eighthree1
1sevenine2
jnsjhqqtj6fourslpqntdzxpfive"""

number_convert = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
                 "nine": "9"}


def find_min(data):
    for number in number_convert.keys():
        if data.startswith(number):
            return number_convert[number]
    return data[0]


def prepare_data(data):
    result = []
    for data in data:
        result.append([find_min(data[index:]) for index in range(0, len(data))])
    return result


def part_1(input_data):
    result = []
    for line in input_data:
        result.append([int(char) for char in line if char.isnumeric()])
    return sum([(int(f"{number[0]}{number[-1]}")) for number in result])


def part_2(input_data):
    prepared_data = prepare_data(input_data)
    return part_1(prepared_data)


if __name__ == '__main__':
    assert (part_1(sample.splitlines()) == 142)
    assert (part_2(sample.splitlines()) == 142)
    assert (part_2(sample2.splitlines()) == 281)
    assert (part_2(sample3.splitlines()) == 179)

    retrieve_input()
    load_data = open(file_path, 'r').read().splitlines()
    print(f"Day 1 part 1: {part_1(load_data)}")
    print(f"Day 1 part 2: {part_2(load_data)}")

