import argparse
from pydoc import locate
from aoc_client import AocClient
from datetime import datetime


class SolutionRunner:

    def __init__(self, day, b, example):
        self.day = day
        self.b = b
        self.example = example
        self.aocClient = AocClient()
        self.solution = self.get_solution(day, b)

    @staticmethod
    def get_solution(day, b):
        day_number = str(day).zfill(2)
        solution_class_name = f'solutions.solution{day_number}b.Solution{day_number}B' if b else f'solutions.solution{day_number}.Solution{day_number}'
        solution_class = locate(solution_class_name)
        if not solution_class:
            raise Exception(f'No solution for day {day}, expected \'{solution_class_name}\' to exist.')
        return solution_class()

    def run(self, submit):
        if self.example:
            input_data = self.aocClient.get_example(self.day)
        else:
            input_data = self.aocClient.get_input(self.day)

        start = datetime.now()
        result = self.solution.solve(input_data)
        duration = datetime.now() - start
        print(f'Execution time: {duration}')
        print(f'OUTPUT:')
        print('>>>', result)

        if submit:
            print('Submitting to Advent of Code!')
            response = self.aocClient.submit(self.day, self.b, result)
            print('Result: ')
            print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download input files for Advent of Code')
    parser.add_argument('day', type=int, help='day number to download input for')
    parser.add_argument('--b', dest='b', action='store_true', help='whether to run the second challenge of the day')
    parser.add_argument('--example', dest='example', action='store_true', help='whether to run the example input')
    parser.add_argument('--submit', dest='submit', action='store_true', help='whether to submit the answer to AoC')
    parser.set_defaults(example=False, b=False, submit=False)
    args = parser.parse_args()

    if args.example and args.submit:
        exit(1)

    runner = SolutionRunner(args.day, args.b, args.example)
    runner.run(args.submit)
