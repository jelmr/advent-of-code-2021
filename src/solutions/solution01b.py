from solutions.solution01 import Solution01
from more_itertools import sliding_window, quantify


class Solution01B(Solution01):

    def solve(self, input_text):
        windows = sliding_window(input_text, 4)
        return quantify(windows, lambda window: int(window[3]) > int(window[0]))
