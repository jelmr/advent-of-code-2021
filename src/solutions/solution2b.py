from solutions.solution2 import Solution2


class Solution2B(Solution2):

    def solve(self, input_text):
        depth = 0
        horizontal_position = 0
        aim = 0

        for instruction in input_text:
            action, step = instruction.split(' ')
            step = int(step)

            match action:
                case 'forward':
                    horizontal_position += step
                    depth += aim * step
                case 'down':
                    aim += step
                case 'up':
                    aim -= step
        return depth * horizontal_position
