from solutions.solution import Solution
import numpy as np
from scipy.signal import convolve2d

KERNEL = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


class Solution11(Solution):
    def solve(self, input_text):
        grid = self.parse_input(input_text)
        total_flashes = 0

        for i in range(100):
            total_flashes += self.simulate_step(grid)

        return total_flashes

    @staticmethod
    def simulate_step(grid):
        num_extra_flashes = 0
        flashed = np.full(grid.shape, False)

        grid += 1

        while True:
            to_flash = flashed ^ (grid > 9)
            grid += convolve2d(to_flash.astype(int), KERNEL, boundary='fill', mode='same')
            flashed |= to_flash
            num_flashes_iteration = to_flash.sum()
            num_extra_flashes += num_flashes_iteration
            if num_flashes_iteration == 0:
                break

        grid[grid > 9] = 0

        return num_extra_flashes

    @staticmethod
    def parse_input(input_text):
        return np.array(list(map(list, input_text)), dtype=int)
