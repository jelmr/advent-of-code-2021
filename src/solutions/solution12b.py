from solutions.solution12 import Solution12


class Solution12B(Solution12):

    def solve(self, input_text):
        caves = self.parse_input(input_text)
        return self.count_paths(caves['start'], caves['end'], Solution12.HashableDict(int), True)
