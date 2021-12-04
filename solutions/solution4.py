from solutions.solution import Solution
import numpy as np
from collections import defaultdict


class Solution4(Solution):
    class Board:
        def __init__(self, numbers):
            size = len(numbers[0])
            numbers_array = np.array(numbers)
            mask = np.zeros(numbers_array.shape)
            self.numbers = np.ma.masked_array(numbers_array, mask=mask, fill_value=0)
            self.columns = np.full(size, size)
            self.rows = self.columns.copy()

    def solve(self, input_text):
        numbers, boards = self.parse_input(input_text)
        index = self.generate_index(boards)

        for number in numbers:
            for (board_idx, x, y) in index[number]:
                board = boards[board_idx]
                board.numbers.mask[x, y] = True
                board.rows[x] -= 1
                board.columns[y] -= 1

                if board.rows[x] == 0 or board.columns[y] == 0:
                    return np.sum(board.numbers) * number

        raise Exception('No solution found...')

    @staticmethod
    def generate_index(boards):
        index = defaultdict(list)
        for board_idx, board in enumerate(boards):
            for (x, y), number in np.ndenumerate(board.numbers.data):
                index[number].append((board_idx, x, y))
        return index

    @staticmethod
    def parse_input(input_text):
        input_length = len(input_text)
        numbers = map(int, input_text[0].split(','))

        boards = []
        current_board_numbers = []
        current_idx = 2  # skip numbers+whiteline

        while current_idx <= input_length:

            if current_idx >= input_length or input_text[current_idx] == '':
                boards.append(Solution4.Board(current_board_numbers))
                current_board_numbers = []
                current_idx += 1
                continue  # skip empty line

            row = list(map(int, filter(None, input_text[current_idx].split(' '))))
            current_board_numbers.append(row)
            current_idx += 1

        return numbers, boards
