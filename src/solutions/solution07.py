from solutions.solution import Solution
import numpy as np


class Solution07(Solution):
    def solve(self, input_text):
        positions = np.array(input_text[0].split(','), dtype=int)
        targets = np.arange(positions.min(), positions.max())
        distances = np.abs(positions[:, np.newaxis] - targets[np.newaxis, :])
        fuel_costs = self.get_fuel_costs(distances)
        return np.min(fuel_costs)

    def get_fuel_costs(self, distances):
        return np.sum(distances, axis=0)
