from solutions.solution09 import Solution09
import numpy as np
import heapq
from functools import reduce
from operator import mul


class Solution09B(Solution09):

    def solve(self, input_text):
        array = self.parse_input(input_text)
        lowpoints = self.get_lowpoints(array)
        largest_basins = []

        for (x, y), is_lowpoint in np.ndenumerate(lowpoints):
            if is_lowpoint:
                size = self.recurse(array, np.full(array.shape, False), -1, x, y)
                heapq.heappush(largest_basins, -size)

        return reduce(mul, map(abs, heapq.nsmallest(3, largest_basins)))

    def recurse(self, array, explored, origin, x, y):
        in_bounds = 0 <= x < array.shape[0] and 0 <= y < array.shape[1]
        if not in_bounds or explored[x, y] or array[x, y] <= origin or array[x, y] == 9:
            return 0
        val = array[x, y]
        explored[x, y] = True
        return 1 + self.recurse(array, explored, val, x + 1, y) + \
               self.recurse(array, explored, val, x - 1, y) + \
               self.recurse(array, explored, val, x, y + 1) + \
               self.recurse(array, explored, val, x, y - 1)
