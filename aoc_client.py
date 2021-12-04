import requests
import os
import configparser
from bs4 import BeautifulSoup

CONFIG_FILE = 'config.ini'
INPUT_DIR = 'inputs'
API_BASE = 'https://adventofcode.com/2021/day'


class AocClient:

    def __init__(self):
        os.makedirs(INPUT_DIR, exist_ok=True)

    def get_input(self, day):
        input_file_name = f'{INPUT_DIR}/{day}.input'

        # Return cached copy
        if os.path.isfile(input_file_name):
            with open(input_file_name, 'r') as input_file:
                return input_file.read().splitlines()

        session_cookie = self.get_session_cookie()

        print(f'Attempting to download input file for day {day}')
        response = requests.get(f'{API_BASE}/{day}/input', cookies={'session': session_cookie})

        if not response.status_code == 200:
            print(f'No input file for day {day}.')
            return

        input_data = response.text

        with open(input_file_name, 'w+') as input_file:
            print(f'Saving input file to `{input_file_name}`')
            input_file.write(input_data)

        return input_data.splitlines()

    def get_example(self, day):
        input_file_name = f'{INPUT_DIR}/{day}.example'

        # Return cached copy
        if os.path.isfile(input_file_name):
            with open(input_file_name, 'r') as input_file:
                return input_file.read().splitlines()

        # Prompt user for the example input
        print('Paste example input:  (Ctrl-D / Ctrl-Z to terminate)')
        example_input = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            example_input.append(line)

        # Write it to file for next time
        with open(input_file_name, 'w+') as input_file:
            input_file.write('\n'.join(example_input))

        return example_input

    def submit(self, day, b, answer):
        session_cookie = self.get_session_cookie()

        data = {
            'level': 2 if b else 1,
            'answer': answer
        }
        response = requests.post(f'{API_BASE}/{day}/answer', cookies={'session': session_cookie}, data=data)

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('main').find('article').find('p').text

    def get_session_cookie(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        if not 'aoc' in config or not 'sessionCookie' in config['aoc']:
            print('You\'ll need to provide your session cookie for adventofcode.com. In your webbrowser: F12 > '
                  'Storage/Application > Cookies.')
            session_cookie = input('Please enter your session cookie: ')
            config['aoc'] = {'sessionCookie': session_cookie}
            with open(CONFIG_FILE, 'w') as configFile:
                config.write(configFile)

        return config['aoc']['sessionCookie']
