import requests
import os
import argparse
import configparser

CONFIG_FILE = 'config.ini'
INPUT_DIR = 'inputs'

class AocClient:

    def __init__(self):
        os.makedirs(INPUT_DIR, exist_ok=True)

    def getInput(self, day):
        input_file_name = f'{INPUT_DIR}/{day}.input'

        # Return cached copy
        if os.path.isfile(input_file_name):
            with open(input_file_name, 'r') as input_file:
                return input_file.read()

        sessionCookie = self.getSessionCookie()

        print(f'Attempting to download input file for day {day}')
        response = requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies={'session': sessionCookie})

        if not response.status_code == 200:
            print(f'No input file for day {day}.')
            return

        input_data = response.text

        with open(input_file_name, 'w+') as input_file:
            print(f'Saving input file to `{input_file_name}`')
            input_file.write(input_data)

        return input_data

    def getExample(self, day):
        pass

    def submit(self, day, answer):
        pass

    def getSessionCookie(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        if not 'aoc' in config or not 'sessionCookie' in config['aoc']:
            print('You\'ll need to provide your session cookie for adventofcode.com. In your webbrowser: F12 > Storage/Application > Cookies.')
            sessionCookie = input('Please enter your session cookie: ')
            config['aoc'] = { 'sessionCookie': sessionCookie }
            with open(CONFIG_FILE, 'w') as configFile:
                config.write(configFile)

        return config['aoc']['sessionCookie']





