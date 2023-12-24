file = open("inputs/DayTwo.txt", "r").read()

dict_of_games_and_pulls = {}
list_of_invalid_games = []
for line in file.split("\n"):
    game_id = line.split(":")[0].replace("Game ", "")
    dict_of_games_and_pulls[game_id] = [[pull for pull in section.split(",")] for section in line.split(":")[1].split(";")]

for game_number, values in dict_of_games_and_pulls.items():
    for section in values:
        blue_counter = 0
        green_counter = 0
        red_counter = 0
        for pull in section:
            if "blue" in pull:
                blue_counter += int(pull.replace("blue", ""))
            elif "red" in pull:
                red_counter += int(pull.replace("red", ""))
            elif "green" in pull:
                green_counter += int(pull.replace("green", ""))
        if blue_counter > 14 or green_counter > 13 or red_counter > 12:
            list_of_invalid_games.append(game_number)

print(sum([element for element in list(range(1, len(file.split("\n")) + 1)) if str(element) not in list_of_invalid_games]))