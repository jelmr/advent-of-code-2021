from solutions.solution03 import Solution03
from more_itertools import quantify


class Solution03B(Solution03):

    def solve(self, input_text):
        oxygen_generator_rating = self.recurse(input_text, 0, True)
        co2_scrubber_rating = self.recurse(input_text, 0, False)
        return oxygen_generator_rating * co2_scrubber_rating

    def recurse(self, subset, digit_idx, most_common):
        one_count = quantify(subset, lambda line: line[digit_idx] == '1')
        digit_to_keep = '1' if most_common == (one_count >= len(subset) / 2) else '0'
        new_subset = [line for line in subset if line[digit_idx] == digit_to_keep]

        if len(new_subset) == 1 or digit_idx >= len(subset[0]):
            return int(new_subset[0], 2)

        return self.recurse(new_subset, digit_idx + 1, most_common)
