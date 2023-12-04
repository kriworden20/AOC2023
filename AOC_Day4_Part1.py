with open("AOC_Day4_Input.txt") as file:
    sum = 0
    for line in file:
        string = line.split(":")
        string = string[1].split("|")
        winning_numbers = string[0].split()
        numbers_you_have = string[1].split()
        power = -1
        for num in numbers_you_have:
            if num in winning_numbers:
                power += 1
        if power >= 0:
            sum += pow(2, power)

print(sum)