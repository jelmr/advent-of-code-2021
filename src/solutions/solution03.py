from solutions.solution import Solution


class Solution03(Solution):

    def solve(self, input_text):
        one_counts = [0] * len(input_text[0])
        input_length = len(input_text)

        for line in input_text:
            for idx, digit in enumerate(line):
                one_counts[idx] += 1 if digit == '1' else 0

        gamma = int(''.join(['1' if count > input_length / 2 else '0' for count in one_counts]), 2)
        epsilon = int(''.join(['1' if count < input_length / 2 else '0' for count in one_counts]), 2)
        return gamma * epsilon
