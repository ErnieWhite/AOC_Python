"""
Advent of Code - Day 03
Year: 2015
"""

import time
from ..utils import utils


def part1(data):
    """
    Solve part 1 of the puzzle
    
    Args:
        data: Input data as string
        
    Returns:
        Solution to part 1
    """
    lines = data.strip().split('\n')
    for line in lines:
        print(line)
    # TODO: Implement solution
    return 0


def part2(data):
    """
    Solve part 2 of the puzzle
    
    Args:
        data: Input data as string
        
    Returns:
        Solution to part 2
    """
    lines = data.strip().split('\n')
    # TODO: Implement solution
    return 0


def main():
    """Main function to run the solutions"""
    # Read input data from file
    try:
        data = read_input("input_03.txt")
    except FileNotFoundError:
        print("Error: input.txt not found")
        print("Please create an input.txt file with your puzzle input")
        return
    
    # Solve and print results
    start = time.time()
    result1 = part1(data)
    stop = time.time()
    print(f"Part 1\tTime: {stop - start:.6f}s\tResult: {result1}")
    
    start = time.time()
    result2 = part2(data)
    stop = time.time()
    print(f"Part 2\t{stop - start:.6f}s\tResult: {result2}")


if __name__ == "__main__":
    main()
