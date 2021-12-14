import numpy as np

from solutions.solution import Solution


class Solution13(Solution):
    def solve(self, input_text):
        points, folds = self.parse_input(input_text)
        self.fold(points, *folds[0])
        return np.unique(points, axis=0).shape[0]

    @staticmethod
    def fold(points, dimension, coordinate):
        points[:, dimension] = coordinate - np.abs(points[:, dimension] - coordinate)

    @staticmethod
    def parse_input(input_text):
        points_text, folds_text = '\n'.join(input_text).split('\n\n')
        points = [line.split(',') for line in points_text.splitlines()]
        folds = []

        for line in folds_text.splitlines():
            fold_info = line.split(' ')[-1].split('=')
            folds.append((0 if fold_info[0] == 'x' else 1, int(fold_info[1])))

        return np.array(points, dtype=int), folds
