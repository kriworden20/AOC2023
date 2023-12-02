# This code is absolutely not written to be efficient.

def check_if_num(line, idx):
    if idx + 2 < len(line):
        if line[idx : idx + 3] == 'one':
            return [3, 1] # length of number string and number itself
        elif line[idx: idx + 3] == 'two':
            return [3, 2]
        if line[idx: idx + 3] == 'six':
            return [3, 6]
    if idx + 4 < len(line):
        if line[idx: idx + 5] == "three":
            return [5, 3]
        if line[idx: idx + 5] == 'seven':
            return [5, 7]
        if line[idx: idx + 5] == 'eight':
            return [5, 8]
    if idx + 3 < len(line):
        if line[idx: idx + 4] == 'four':
            return [4, 4]
        elif line[idx: idx + 4] == 'five':
            return [4, 5]
        elif line[idx: idx + 4] == 'nine':
            return [4, 9]

    return None

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sum = 0
with open("AOC_Day1_Input.txt") as file:
    for line in file:
        start_idx = 0
        end_idx = len(line) - 1
        first_num = None
        second_num = None
        while start_idx < len(line) and end_idx >= 0 and (first_num == None or second_num == None):
            temp = line[start_idx]
            if first_num == None:
                if not temp.isdigit():
                    result = check_if_num(line, start_idx)
                    if result != None:
                        first_num = result[1]
                        start_idx += result[0]
                elif temp.isdigit():
                    first_num = int(temp)
            temp = line[end_idx]
            if second_num == None:
                if not temp.isdigit():
                    result = check_if_num(line, end_idx)
                    if result != None:
                        second_num = result[1]
                elif temp.isdigit():
                    second_num = int(temp)
            start_idx += 1
            end_idx -= 1
        if first_num != None and second_num != None:
            num = first_num * 10 + second_num
            sum += num

print('answer: ' + str(sum))