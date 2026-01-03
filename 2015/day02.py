"""
Advent of Code - Day 02
Year: 2015
"""

import time


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
        print(line.split('x'))


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
        with open("input_02.txt", "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found")
        print("Please create an input.txt file with your puzzle input")
        return
    
    # Solve and print results
    start = time.time()
    result1 = part1(data)
    print(f"Time taken for Part 1: {time.time() - start:.6f} seconds")
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    start = time.time()
    print(f"Part 2: {result2}")
    print(f"Time taken for Part 2: {time.time() - start:.6f} seconds")


if __name__ == "__main__":
    main()
