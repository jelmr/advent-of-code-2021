from solutions.solution1 import Solution1
from more_itertools import sliding_window, quantify


class Solution1B(Solution1):

    def solve(self, input_text):
        windows = sliding_window(input_text, 4)
        return quantify(windows, lambda window: int(window[3]) > int(window[0]))
