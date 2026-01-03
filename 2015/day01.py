"""
Advent of Code 2015 - Day 1: Not Quite Lisp
https://adventofcode.com/2015/day/1
"""
import time


def part1(data):
    """
    Calculate the floor Santa ends up on.
    '(' means go up one floor, ')' means go down one floor.
    
    Args:
        data: Input data as string
        
    Returns:
        Final floor number
    """
    floor = 0
    for char in data.strip():
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor


def part2(data):
    """
    Find the position of the first character that causes Santa
    to enter the basement (floor -1).
    
    Args:
        data: Input data as string
        
    Returns:
        Position (1-indexed) of the first basement-causing character
    """
    floor = 0
    for i, char in enumerate(data.strip(), 1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        
        if floor == -1:
            return i
    return -1


def main():
    """Main function to run the solutions"""
    # Read input data from file
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        # Use example data if input file not found
        print("Warning: input.txt not found, using example data")
        data = "(())"
    
    # Solve and print results
    start_time = time.time()
    result1 = part1(data)
    print(f"Time taken for Part 1: {time.time() - start_time:.6f} seconds")
    print(f"Part 1: {result1}")
    
    start_time = time.time()
    result2 = part2(data)
    print(f"Time taken for Part 2: {time.time() - start_time:.6f} seconds")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
