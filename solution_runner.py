import requests
import os
import argparse
from pydoc import locate
from aoc_client import AocClient


class SolutionRunner:

    def __init__(self, day, example):
        self.day = day
        self.example = example
        self.aocClient = AocClient()
        self.solution = SolutionRunner.getSolution(day)

    def getSolution(day):
        solutionClassName = f'solutions.solution{day}.Solution{day}'
        solutionClass = locate(solutionClassName)
        if not solutionClass:
            raise Exception(f'No solution for day {day}, expected \'{solutionClassName}\' to exist.')
        return solutionClass()

    def run(self):
        input_data = self.aocClient.getInput(self.day)
        self.solution.solve(input_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download input files for Advent of Code')
    parser.add_argument('day', type=int, help='day number to download input for')
    parser.add_argument('--example', dest='example', action='store_true', help='whether to run the example input')
    parser.set_defaults(example=False)
    args = parser.parse_args()

    SolutionRunner(args.day, args.example).run()
