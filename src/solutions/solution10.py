from solutions.solution import Solution

OPEN_TO_CLOSE = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
}
CLOSE_TO_OPEN = {v: k for k, v in OPEN_TO_CLOSE.items()}
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


class Solution10(Solution):
    def solve(self, input_text):
        return sum([self.check_line(line)[0] for line in input_text])

    @staticmethod
    def check_line(line):
        operators = []
        for c in line:
            if c in OPEN_TO_CLOSE:
                operators.append(c)
            elif c in CLOSE_TO_OPEN and CLOSE_TO_OPEN[c] == operators[-1]:
                operators.pop()
            else:
                return POINTS[c], operators

        return 0, operators
