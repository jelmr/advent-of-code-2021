from solutions.solution import Solution
import numpy as np
from scipy.signal import convolve2d

KERNELS = [
    [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
]


class Solution09(Solution):
    def solve(self, input_text):
        array = self.parse_input(input_text)
        lowpoints = self.get_lowpoints(array)
        return sum(array[lowpoints] + 1)

    @staticmethod
    def parse_input(input_text):
        return np.array(list(map(list, input_text)), dtype=int)

    @staticmethod
    def get_lowpoints(array):
        result = np.full(array.shape, True)
        for kernel in KERNELS:
            result &= convolve2d(array, kernel, boundary='fill', fillvalue=99, mode='same') > array
        return result
