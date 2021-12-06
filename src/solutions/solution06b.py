from solutions.solution06 import Solution06
from collections import Counter, defaultdict


class Solution06B(Solution06):

    def solve(self, input_text):
        fish = list(map(int, input_text[0].split(',')))
        fish_counts = defaultdict(int, Counter(fish).items())
        return self.simulate(fish_counts, 256)
