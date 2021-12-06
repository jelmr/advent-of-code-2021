from solutions.solution import Solution
from collections import Counter, defaultdict


class Solution06(Solution):
    def solve(self, input_text):
        fish = list(map(int, input_text[0].split(',')))
        fish_counts = defaultdict(int, Counter(fish).items())
        return self.simulate(fish_counts, 80)

    def simulate(self, fish, days):
        for day in range(days):
            new_fish = defaultdict(int)
            for fish_value, fish_count in fish.items():
                if fish_value > 0:
                    new_fish[fish_value - 1] += fish_count
                else:
                    new_fish[6] += fish_count
                    new_fish[8] += fish_count
            fish = new_fish
        return sum(fish.values())
