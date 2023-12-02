############
# Part 1
############
# He forgot to parse the line. I should ask for the parsing.
import re

def parse_game_data(game_string):
    # Regular expression to match game records
    game_pattern = r'Game (\d+): (.+?)(?:;|$)'
    set_pattern = r'(\d+) (red|green|blue)'

    games = re.findall(game_pattern, game_string)
    parsed_games = []

    for game in games:
        game_id = int(game[0])
        sets = game[1].split('; ')
        game_data = []

        for set in sets:
            set_data = re.findall(set_pattern, set)
            set_dict = {color: int(number) for number, color in set_data}
            game_data.append(set_dict)

        parsed_games.append((game_id, game_data))

    return parsed_games

# Example usage
game_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green; Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue; Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red; Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red; Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
parsed_games = parse_game_data(game_string)

print(parsed_games)

def is_game_possible(game_data, red_cubes, green_cubes, blue_cubes):
    for set in game_data:
        if set.get('red', 0) > red_cubes or set.get('green', 0) > green_cubes or set.get('blue', 0) > blue_cubes:
            return False
    return True

def sum_of_possible_game_ids(games):
    possible_game_ids = []

    for game in games:
        game_id, game_data = game
        if is_game_possible(game_data, 12, 13, 14):
            possible_game_ids.append(game_id)

    return sum(possible_game_ids)

# Example usage
games_data = [
    (1, [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]),
    (2, [{'blue': 1, 'green': 2}, {'green': 3, 'blue': 4, 'red': 1}, {'green': 1, 'blue': 1}]),
    (3, [{'green': 8, 'blue': 6, 'red': 20}, {'blue': 5, 'red': 4, 'green': 13}, {'green': 5, 'red': 1}]),
    (4, [{'green': 1, 'red': 3, 'blue': 6}, {'green': 3, 'red': 6}, {'green': 3, 'blue': 15, 'red': 14}]),
    (5, [{'red': 6, 'blue': 1, 'green': 3}, {'blue': 2, 'red': 1, 'green': 2}])
]

print(sum_of_possible_game_ids(games_data))

############
# Part 2
############

def minimum_cubes_per_game(games):
    powers = []

    for game in games:
        max_red, max_green, max_blue = 0, 0, 0
        print(game[1])
        for set in game[1]:
            max_red = max(max_red, set.get('red', 0))
            max_green = max(max_green, set.get('green', 0))
            max_blue = max(max_blue, set.get('blue', 0))

        power = max_red * max_green * max_blue
        powers.append(power)
    print(powers)
    return sum(powers)

# Using the previously defined parse_game_data function
game_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green; Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue; Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red; Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red; Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
parsed_games = parse_game_data(game_string)

total_power = minimum_cubes_per_game(parsed_games)
print(total_power)
