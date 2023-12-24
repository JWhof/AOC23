file = open("inputs/DayTwo.txt", "r").read()
dict_of_games_and_pulls = {}
list_of_powers = []
game_id = 1

for line in file.split("\n"):
    game_id = line.split(":")[0].replace("Game ", "")
    dict_of_games_and_pulls[game_id] = [[pull for pull in section.split(",")] for section in line.split(":")[1].split(";")]

for value in dict_of_games_and_pulls.values():
    blue_max = 0
    green_max = 0
    red_max = 0
    for section in value:
        for pull in section:
            if "blue" in pull:
                if blue_max < int(pull.replace("blue", "")):
                    blue_max = int(pull.replace("blue", ""))
            elif "red" in pull:
                if red_max < int(pull.replace("red", "")):
                    red_max = int(pull.replace("red", ""))
            elif "green" in pull:
                if green_max < int(pull.replace("green", "")):
                    green_max = int(pull.replace("green", ""))
    list_of_powers.append(blue_max*red_max*green_max)

print(sum(list_of_powers))