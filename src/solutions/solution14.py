from collections import defaultdict

from solutions.solution import Solution


class Solution14(Solution):

    def __init__(self):
        self.num_iterations = 10

    def solve(self, input_text):
        pair_counts, insertions = self.parse_input(input_text)

        for i in range(self.num_iterations):
            pair_counts = self.perform_step(pair_counts, insertions)

        letter_counts = self.get_letter_counts(pair_counts, input_text)
        return max(letter_counts) - min(letter_counts)

    @staticmethod
    def get_letter_counts(pair_counts, input_text):
        letter_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            letter_counts[pair[0]] += count
            letter_counts[pair[1]] += count

        # Divide by 2 because each letter is part of two pairs, except for the first- and last letter
        letter_counts[input_text[0][0]] += 1
        letter_counts[input_text[0][-1]] += 1
        return list(map(lambda count: count // 2, letter_counts.values()))

    @staticmethod
    def perform_step(pair_counts, insertions):
        new_pair_counts = defaultdict(int)

        for pair, count in pair_counts.items():
            mapped_letter = insertions[pair]
            if mapped_letter:
                new_pair_counts[pair[0] + mapped_letter] += count
                new_pair_counts[mapped_letter + pair[1]] += count
            else:
                new_pair_counts[pair] += count

        return new_pair_counts

    @staticmethod
    def parse_input(input_text):
        counts = defaultdict(int)

        for pair in zip(input_text[0], input_text[0][1:]):
            pair_str = ''.join(pair)
            counts[pair_str] += 1

        insertion_map = defaultdict(dict)
        for line in input_text[2:]:
            rule, to = line.split(' -> ')
            insertion_map[rule] = to

        return counts, insertion_map
