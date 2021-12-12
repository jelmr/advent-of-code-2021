from collections import defaultdict
from dataclasses import dataclass
from functools import cache

from solutions.solution import Solution


class Solution12(Solution):
    @dataclass
    class Cave:
        name: str
        is_small: bool
        neighbours: list

        def __hash__(self):
            return hash(self.name)

    class HashableDict(defaultdict):
        def __hash__(self):
            return hash(tuple(self.items()))

    def solve(self, input_text):
        caves = self.parse_input(input_text)
        return self.count_paths(caves['start'], caves['end'], Solution12.HashableDict(int), False)

    @cache
    def count_paths(self, current, target, num_visits, bonus_visit_available):
        if current.is_small:
            if num_visits[current] >= 1:
                if bonus_visit_available and current.name != 'start':
                    bonus_visit_available = False
                else:
                    return 0
            num_visits[current] += 1

        if current == target:
            num_paths = 1
        else:
            num_paths = sum(self.count_paths(n, target, num_visits, bonus_visit_available) for n in current.neighbours)

        if current.is_small:
            num_visits[current] -= 1

        return num_paths

    @staticmethod
    def parse_input(input_text):
        caves = {}

        for line in input_text:
            vertices = line.split('-')

            # create caves if needed
            for vertex in vertices:
                if vertex not in caves:
                    caves[vertex] = Solution12.Cave(vertex, vertex.islower(), [])

            # connect neighbours
            caves[vertices[0]].neighbours.append(caves[vertices[1]])
            caves[vertices[1]].neighbours.append(caves[vertices[0]])

        return caves
