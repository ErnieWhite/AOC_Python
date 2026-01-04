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

    total_area = 0
    for line in lines:
        length, width, height = map(int, line.split('x'))
        area1 = length * width
        area2 = width * height
        area3 = height * length
        extra = min (area1, area2, area3)
        total_area += 2 * (area1 + area2 + area3) + extra
    return total_area


def ribbon_needed(side_lengths):
    sides = sorted(side_lengths)
    return  2*sum(sides[:2]) + sides[0] * sides[1] * sides[2]


def part2(data):
    """
    Solve part 2 of the puzzle

    Formulas:
    - Smallest perimeter: 2 * (sum of the two smallest sides)
    - Volume: length * width * height
    
    Args:
        data: Input data as string
        
    Returns:
        Solution to part 2
    """
    lines = data.strip().split('\n')
    total_ribbon = 0
    for line in lines:
        box_sides = list(map(int, line.split("x")))
        total_ribbon += ribbon_needed(box_sides)
    return total_ribbon 


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
    stop = time.time()
    print(f"Part 1\tTime: {stop - start:.6f}s\tResult: {result1}")
    
    start = time.time()
    result2 = part2(data)
    stop = time.time() 
    print(f"Part 2\tTime: {stop - start:.6f}s\tResult: {result2}")


if __name__ == "__main__":
    main()
