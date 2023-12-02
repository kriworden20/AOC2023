import copy


sum = 0
with open("AOC_Day1_Part1_Input.txt") as file:
    for line in file:
        start_idx = 0
        end_idx = len(line) - 1
        first_num = None
        second_num = None
        while start_idx < len(line) and end_idx >= 0 and (first_num == None or second_num == None):
            if first_num == None and line[start_idx].isdigit():
                first_num = int(line[start_idx])
            if second_num == None and line[end_idx].isdigit():
                second_num = int(line[end_idx])
            start_idx += 1
            end_idx -= 1
        if first_num != None and second_num != None:
            num = first_num * 10 + second_num
            sum += num

print('answer: ' + str(sum))


