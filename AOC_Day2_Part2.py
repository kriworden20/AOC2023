with open("AOC_Day2_Input.txt") as file:
    sum = 0
    for line in file:
        cubes_dict = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        string = line.split(":")
        sets = string[1].split(";")
        for set in sets:
            set = set.split(',')
            for draw in set:
                temp = draw.split()
                num_cubes = int(temp[0])
                color = temp[1]
                if num_cubes > cubes_dict[color]:
                    cubes_dict[color] = num_cubes
    
        power = 1
        for color in cubes_dict:
            power *= cubes_dict[color]
        sum += power

    print(sum)