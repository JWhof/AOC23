file = open("inputs/DayOne.txt", "r").read()
number_word_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

list_of_ints = []
list2_of_ints = []
final_2_ints = []

for line in file.split("\n"):
    dict_of_indexes = {}
    k = -1
    for number_word in number_word_dict:
        if number_word in line:
            dict_of_indexes[line.index(number_word)] = number_word

    dict_of_indexes = dict(sorted(dict_of_indexes.items()))
    
    if len(dict_of_indexes) > 1 and [char for char in line.replace(dict_of_indexes[list(dict_of_indexes.keys())[0]], str(number_word_dict[dict_of_indexes[list(dict_of_indexes.keys())[0]]])) if str(char).isdigit()][0] == number_word_dict[dict_of_indexes[list(dict_of_indexes.keys())[0]]]:
        while line.index(dict_of_indexes[list(dict_of_indexes.keys())[k-1]]) + len(dict_of_indexes[list(dict_of_indexes.keys())[k-1]]) >= line.index(dict_of_indexes[list(dict_of_indexes.keys())[k]]):
            dict_of_indexes.pop(list(dict_of_indexes.keys())[k-1])
            if len(dict_of_indexes) <= 1:
                break

    if dict_of_indexes != {}:
        line = line.replace(dict_of_indexes[min(list(dict_of_indexes.keys()))], str(number_word_dict[dict_of_indexes[min(list(dict_of_indexes.keys()))]]))
        line = line.replace(dict_of_indexes[list(dict_of_indexes.keys())[-1]], str(number_word_dict[dict_of_indexes[list(dict_of_indexes.keys())[-1]]]))

    list2_of_ints.append(int(f"{[char for char in line if str(char).isdigit()][0]}{[char for char in line if str(char).isdigit()][-1]}"))
print(sum(list2_of_ints))
    