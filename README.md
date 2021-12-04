### To setup:
```
python3.10 -m venv aoc
aoc/bin/pip install -r requirements.txt
```

### To run a solution for day `day`, using the example input
```
aoc/bin/python src/solution_runner <day> --example
```
e.g.
```
aoc/bin/python src/solution_runner 4 --example
```

You can delete the `.example` files from the `inputs` directory to reset examples.

### To run a solution for day `day`, using your actual input
```
aoc/bin/python src/solution_runner <day>
```

### To run Solution B (part two) for day `day`
Add the `--b` flag:
```
aoc/bin/python src/solution_runner <day> --b
aoc/bin/python src/solution_runner <day> --b --example
```

### To  submit your solution:
```
aoc/bin/python src/solution_runner <day> [--b] --submit
```

