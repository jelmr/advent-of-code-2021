from solutions.solution import Solution


class Solution2(Solution):

    def solve(self, input_text):
        depth = 0
        horizontal_position = 0

        for instruction in input_text:
            action, step = instruction.split(' ')
            step = int(step)

            match action:
                case 'forward':
                    horizontal_position += step
                case 'down':
                    depth += step
                case 'up':
                    depth -= step
        return depth * horizontal_position
