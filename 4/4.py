import numpy as np
from typing import List, Set, Dict, Tuple, Optional
from dataclasses import dataclass
from colorama import init, Style, Fore

init()


@dataclass
class BingoField:
    val: int
    marked: bool


class Board:
    def __init__(self, board_lines):
        self._d = [[BingoField(int(number), False) for number in line.rstrip().split()]
                   for line in board_lines]

    def mark(self, call):
        for row in self._d:
            for field in row:
                if field.val == call:
                    field.marked = True

    def finished(self):
        def _finished_field_sequence(sequences):
            for seq in sequences:
                if len([field.val for field in seq if field.marked]) == 5:
                    return True
            return False

        return _finished_field_sequence(self._d) or _finished_field_sequence(zip(*self._d))

    def score(self):
        score = 0

        for row in range(5):
            for column in range(5):
                if not self._d[row][column].marked:
                    score += self._d[row][column].val

        return score

    def print(self):
        for row in self._d:
            print('\t'.join(
                [Fore.RED + str(field.val) + Style.RESET_ALL if field.marked else str(field.val) for field in row]))


def process_calls(calls: List[int], boards: List[Board]):
    for call in calls:
        for board in boards:
            board.mark(call)
            if board.finished():
                return call * board.score()


filename = __file__.replace('py', 'txt')

with open(filename) as file:
    lines = file.readlines()

calls = [int(call) for call in lines[0].rstrip().split(',')]
boards = [Board(lines[starting_line:starting_line + 5])
          for starting_line in range(2, len(lines), 6)]

print(calls)

print(process_calls(calls, boards))
