from solutions.solution import Solution
from more_itertools import quantify


class Solution08(Solution):
    def solve(self, input_text):
        outputs = map(lambda line: line.split(' | ')[1].split(' '), input_text)
        return quantify([item for line in outputs for item in line], lambda item: len(item) in [2,3,4,7])

