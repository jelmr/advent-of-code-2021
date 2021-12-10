from solutions.solution10 import Solution10

POINTS = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


class Solution10B(Solution10):

    def solve(self, input_text):
        scores = []
        for line in input_text:
            corrupt_score, operators = self.check_line(line)

            if corrupt_score > 0:
                continue

            score = 0
            for operator in operators[::-1]:
                score *= 5
                score += POINTS[operator]
            scores.append(score)

        return sorted(scores)[len(scores) // 2]
