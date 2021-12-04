from solutions.solution04 import Solution04
import numpy as np


class Solution04B(Solution04):

    def solve(self, input_text):
        numbers, boards = self.parse_input(input_text)
        numbers = list(numbers)
        index = self.generate_index(boards)
        remaining_boards = set(range(len(boards)))

        for number in numbers:
            for (board_idx, x, y) in index[number]:
                board = boards[board_idx]
                board.numbers.mask[x, y] = True
                board.rows[x] -= 1
                board.columns[y] -= 1

                # board has won, remove it from set
                if board.rows[x] == 0 or board.columns[y] == 0:
                    if board_idx in remaining_boards:
                        remaining_boards.remove(board_idx)

                    if len(remaining_boards) == 0:
                        return np.sum(board.numbers) * number

        raise Exception('No solution found...')
