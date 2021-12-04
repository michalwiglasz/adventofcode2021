#!/usr/bin/env python3

import re


def load():
    boards = set()

    with open('04.txt', 'rt') as f:
        numbers = [int(n) for n in f.readline().split(',')]

        board = []
        for line in (x.strip() for x in f):
            if not line:
                if board:
                    boards.add(tuple(board))
                board = []
                continue
            board.append(tuple(int(n) for n in re.split(r'\s+', line)))

        if board:
            boards.add(tuple(board))

    return boards, numbers


def check_boards(boards, called):
    for board in boards:
        if check_board(board, called):
            yield board
    else:
        return None


def check_board(board, called):
    # check rows
    for row in board:
        if all(n in called for n in row):
            return True

    # check cols
    for cn in range(len(board)):
        col = tuple(row[cn] for row in board)
        if all(n in called for n in col):
            return True

    return False


def get_score(board, num, called):
     unmarked_nums = [n for row in board for n in row if n not in called]
     return sum(unmarked_nums) * num


boards, numbers = load()
called = set()

for num in numbers:
    called.add(num)
    winners = list(check_boards(boards, called))
    for winner in winners:
        score = get_score(winner, num, called)
        print("win:", winner, "/ total", len(boards), "/ nums", len(called), "/ ", num, "/ score", score)
        boards.remove(winner)
