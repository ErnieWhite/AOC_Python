# Advent of Code Solutions in Python

This repository contains my solutions to [Advent of Code](https://adventofcode.com/) problems from 2015 to 2025, implemented in Python.

## Structure

The repository is organized by year, with each year containing solutions for the daily puzzles:

```
AOC_Python/
├── 2015/
│   ├── day01.py
│   ├── day02.py
│   └── ...
├── 2016/
├── 2017/
├── ...
└── 2025/
```

## Usage

Each day's solution is contained in its own Python file. To run a solution:

```bash
python 2015/day01.py
```

### Solution Template

Each solution file typically follows this structure:

```python
def part1(data):
    """Solve part 1 of the puzzle"""
    # Implementation here
    pass

def part2(data):
    """Solve part 2 of the puzzle"""
    # Implementation here
    pass

if __name__ == "__main__":
    # Read input data
    with open("input.txt", "r") as f:
        data = f.read().strip()
    
    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
```

## Input Files

Input files are stored alongside the solution files as `input.txt` or can be named specifically (e.g., `day01_input.txt`).

## Progress

- 2015: [ ] 0/25
- 2016: [ ] 0/25
- 2017: [ ] 0/25
- 2018: [ ] 0/25
- 2019: [ ] 0/25
- 2020: [ ] 0/25
- 2021: [ ] 0/25
- 2022: [ ] 0/25
- 2023: [ ] 0/25
- 2024: [ ] 0/25
- 2025: [ ] 0/25

## Requirements

- Python 3.6+

Additional requirements will be documented in `requirements.txt` as needed.

## License

This project is licensed under the MIT License - see the LICENSE file for details.