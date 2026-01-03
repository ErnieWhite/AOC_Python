"""
Common utility functions for Advent of Code solutions
"""

from typing import List, Tuple, Set, Dict, Any
from collections import defaultdict, Counter, deque
import re


def read_input(filename: str = "input.txt") -> str:
    """
    Read input file and return as string
    
    Args:
        filename: Name of the input file
        
    Returns:
        Contents of the file as a string
    """
    with open(filename, "r") as f:
        return f.read()


def read_lines(filename: str = "input.txt", strip: bool = True) -> List[str]:
    """
    Read input file and return as list of lines
    
    Args:
        filename: Name of the input file
        strip: Whether to strip whitespace from each line
        
    Returns:
        List of lines from the file
    """
    with open(filename, "r") as f:
        lines = f.readlines()
        if strip:
            return [line.strip() for line in lines]
        return lines


def read_int_list(filename: str = "input.txt") -> List[int]:
    """
    Read input file and return as list of integers (one per line)
    
    Args:
        filename: Name of the input file
        
    Returns:
        List of integers
    """
    return [int(line.strip()) for line in read_lines(filename)]


def read_grid(filename: str = "input.txt") -> List[List[str]]:
    """
    Read input file and return as 2D grid
    
    Args:
        filename: Name of the input file
        
    Returns:
        2D list representing the grid
    """
    lines = read_lines(filename)
    return [list(line) for line in lines]


def get_neighbors(x: int, y: int, diagonal: bool = False) -> List[Tuple[int, int]]:
    """
    Get neighboring coordinates
    
    Args:
        x: X coordinate
        y: Y coordinate
        diagonal: Whether to include diagonal neighbors
        
    Returns:
        List of neighboring coordinates
    """
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    if diagonal:
        neighbors.extend([(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)])
    return neighbors


def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """
    Calculate Manhattan distance between two points
    
    Args:
        p1: First point (x, y)
        p2: Second point (x, y)
        
    Returns:
        Manhattan distance
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def extract_ints(text: str) -> List[int]:
    """
    Extract all integers from a string
    
    Args:
        text: Input string
        
    Returns:
        List of integers found in the string
    """
    return [int(x) for x in re.findall(r'-?\d+', text)]


def chunks(lst: List[Any], n: int) -> List[List[Any]]:
    """
    Split a list into chunks of size n
    
    Args:
        lst: Input list
        n: Chunk size
        
    Returns:
        List of chunks
    """
    return [lst[i:i + n] for i in range(0, len(lst), n)]
