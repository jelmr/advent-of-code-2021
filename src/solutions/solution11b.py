from solutions.solution11 import Solution11


class Solution11B(Solution11):

    def solve(self, input_text):
        grid = self.parse_input(input_text)
        step = 0

        while self.simulate_step(grid) != grid.size:
            step += 1

        return step + 1
