cards = {}
scratchcards = 0
with open("test.txt") as file:
    for line in file:
        scratchcards += 1
        string = line.split(":")
        card_num = string[0].split()[1]
        string = string[1].split("|")
        winning_numbers = string[0].split()
        numbers_you_have = string[1].split()
        cards[card_num] = 0
        for num in numbers_you_have:
            if num in winning_numbers:
                cards[card_num] += 1

copies = {}
for i in range(1, scratchcards + 1):
    copies[str(i)] = 0

for card_num in cards:
    for i in range(1, cards[card_num] + 1):
        cards[str(i)] += 1
print(cards)
print(sum)