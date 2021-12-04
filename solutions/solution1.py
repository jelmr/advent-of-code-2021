from solutions.solution import Solution
from itertools import pairwise
from more_itertools import quantify


class Solution1(Solution):

    def solve(self, input_text):
        return quantify(pairwise(input_text), lambda pair: int(pair[1]) > int(pair[0]))
