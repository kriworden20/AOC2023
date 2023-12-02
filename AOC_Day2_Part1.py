cubes_dict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open("AOC_Day2_Input.txt") as file:
    sum = 0
    for line in file:
        possible = True
        string = line.split(":")
        ID = int(string[0].split("Game ")[1])
        sets = string[1].split(";")
        for set in sets:
            set = set.split(',')
            for draw in set:
                temp = draw.split()
                num_cubes = int(temp[0])
                color = temp[1]
                if num_cubes > cubes_dict[color]:
                    possible = False
                    break
            if not possible: break
        if possible:
            sum += ID

    print(sum)