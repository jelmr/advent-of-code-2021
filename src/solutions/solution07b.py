from solutions.solution07 import Solution07
import numpy as np


class Solution07B(Solution07):

    def get_fuel_costs(self, distances):
        return np.sum(distances * (distances + 1) // 2, axis=0)
