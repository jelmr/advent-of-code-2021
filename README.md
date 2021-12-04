To setup:
```
python3.10 -m venv aoc
aoc/bin/pip install -r requirements.txt
```

To run a solution for day `day`, using the example input
```
aoc/bin/python solution_runner <day> --example
```

To run a solution for day `day`, using your actual input
```
aoc/bin/python solution_runner <day>
```

To run Solution B (part two) for day `day`, add the `--b` flag:
```
aoc/bin/python solution_runner <day> --b
aoc/bin/python solution_runner <day> --b --example
```

To  submit your solution:
```
aoc/bin/python solution_runner <day> [--b] --submit
```

