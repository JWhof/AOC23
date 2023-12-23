file = open("inputs/DayOne.txt", "r").read()

list_of_ints = []
list2_of_ints = []
for line in file.split("\n"):
    for char in line:
        if char.isdigit():
            list_of_ints.append(char)
    list2_of_ints.append(int(f"{list_of_ints[0]}{list_of_ints[-1]}"))
    list_of_ints = []
print(sum(list2_of_ints))
