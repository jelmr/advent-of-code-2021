from solutions.solution import Solution
import numpy as np


class Solution05(Solution):

    def solve(self, input_text):
        return self.count_overlaps(input_text, False)

    def count_overlaps(self, input_text, consider_diagonal_lines):
        lines, min_x, max_x, min_y, max_y = self.parse_input(input_text)
        offset = np.array([min_x, min_y])
        board = np.zeros((max_x - min_x + 1, max_y - min_y + 1))

        if not consider_diagonal_lines:
            lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

        self.fill_board(board, offset, lines)

        return board[board > 1].shape[0]

    def fill_board(self, board, offset, lines):
        for start, end in lines:
            delta = end - start
            largest_delta = np.absolute(delta).max()
            step = delta // largest_delta

            for i in range(largest_delta + 1):
                board[tuple(start - offset)] += 1
                start += step
        return board

    def parse_input(self, input_text):
        min_x = min_y = float('inf')
        max_x = max_y = 0
        lines = []

        def update_bounds(x, y):
            nonlocal min_x, max_x, min_y, max_y
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y

        for line in input_text:
            start_str, end_str = line.split(' -> ')
            start = list(map(int, start_str.split(',')))
            end = list(map(int, end_str.split(',')))
            update_bounds(start[0], start[1])
            update_bounds(end[0], end[1])
            lines.append((np.array(start), np.array(end)))

        return lines, min_x, max_x, min_y, max_y