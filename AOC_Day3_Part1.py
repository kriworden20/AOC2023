# ascii values 33 - 45 and 58 - 126 count as symbols
symbol_asciis = range(1,46)
symbol_asciis = list(symbol_asciis) + [value for value in range(58,127)]

# ascii range for digits 0 - 9 is 48 - 57
digit_asciis = range(48, 58)

schematic = []

with open("AOC_Day3_Input.txt") as file:
    for line in file:
        schematic.append(line.rstrip())

sum = 0

def check_same_line(row, start, end, symbol_asciis):
    # check left
    if start != 0 and ord(row[start - 1]) in symbol_asciis:
        return True

    # check right
    if end < len(row) - 1 and ord(row[end + 1]) in symbol_asciis:
        return True
    
def check_below(row, start, end, symbol_asciis):
    # check bottom left
    if start != 0 and ord(row[start - 1]) in symbol_asciis:
        return True

    # check bottom right
    if end < len(row) - 1 and ord(row[end + 1]) in symbol_asciis:
        return True
    
    # check below each digit
    for i in range(start, end + 1):
        if ord(row[i]) in symbol_asciis:
            return True

def check_above(row, start, end, symbol_asciis):
    # check top left
    if start != 0 and ord(row[start - 1]) in symbol_asciis:
        return True
    
    # check top right
    if end < len(row) - 1 and ord(row[end + 1]) in symbol_asciis:
        return True
    
    # check above each digit
    for i in range(start, end + 1):
        if ord(row[i]) in symbol_asciis:
            return True

f = open("demofile2.txt", "a")

# check first line
for row_idx, row in enumerate(schematic):
    char_idx = 0
    print("row: " + str(row_idx))
    f.write("row: " + str(row_idx) + "\n")
    while char_idx < len(row):
        char = row[char_idx]
        start = char_idx
        end = char_idx
        # if char is a digit
        num = ''
        while True:
            if ord(char) >= 48 and ord(char) <= 57:
                num += char
                end = char_idx
            else: break
            if char_idx + 1 == len(row): break
            
            char_idx += 1
            char = row[char_idx]

        if num == '': 
            char_idx += 1
            continue

        print(num)
        f.write(num + "\n")

        if check_same_line(schematic[row_idx], start, end, symbol_asciis):
            sum += int(num)
            print("counted: " + num)
            f.write("counted: " + num+  "\n")
        elif row_idx + 1 < len(schematic) and check_below(schematic[row_idx + 1], start, end, symbol_asciis):
            sum += int(num)
            print("counted: " + num)
            f.write("counted: " + num + "\n")

        elif row_idx > 0 and check_above(schematic[row_idx - 1], start, end, symbol_asciis):
            sum += int(num)
            print("counted: " + num)
            f.write("counted: " + num + "\n")


        char_idx += 1
        
print(sum)
f.close()