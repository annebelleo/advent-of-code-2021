content_list = open("day4.txt", "r").read().splitlines()
bingo_markers = content_list[0].split(',')
bingo_rows = content_list[2::]  # get rows of cards
bingo_cards = {}
card_number = 0

for i in range(0, len(bingo_rows)):  # separate bingo cards
    if not bingo_cards:  # if dict of cards is empty
        bingo_cards[card_number] = []
    elif len(bingo_cards[card_number]) > 4:  # every card must have exactly 5 rows
        card_number += 1
        bingo_cards[card_number] = []
    elif bingo_rows[i]:  # if string is not empty
        bingo_cards[card_number].append(bingo_rows[i])


# note: bingo rows only include non-empty strings, so lengths won't match

for card in range(0, len(bingo_cards)):  # separate numbers in rows
    for row in range(5):
        bingo_cards[card][row] = bingo_cards[card][row].split(" ")
        bingo_cards[card][row] = list(
            filter(None, bingo_cards[card][row]))  # remove empty spaces


def check_bingo_horizontal(list):
    if all(x == list[0] for x in list):
        return True


def check_bingo_vertical(card):
    for i in range(5):
        iteration = 0
        for row in range(0, len(card)):
            if not card[row][i] != 'yes':
                iteration += 1
            if iteration == 5:
                return True


def run_game(markers, cards):
    for marker in markers:  # check if numbers match
        for card in range(0, len(cards)):
            for row in range(5):
                for value in range(5):
                    if marker == cards[card][row][value]:
                        cards[card][row][value] = 'yes'
                    if check_bingo_horizontal(cards[card][row]) is True or check_bingo_vertical(cards[card]) is True:
                        return marker, cards[card]


marker_board = run_game(bingo_markers, bingo_cards)
marker = marker_board[0]
board = marker_board[1]
sum_numbers = 0
for row in range(len(board)):
    for i in range(len(board[row])):
        if board[row][i] != 'yes':
            sum_numbers += int(board[row][i])
print(sum_numbers*int(marker))
