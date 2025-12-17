"""Utility functions for Advent of Code solutions."""

from pathlib import Path
from typing import List


def read_input(day: int) -> str:
    """Read the input file for a given day.

    Args:
        day: The day number (1-25)

    Returns:
        The contents of the input file as a string
    """
    input_path = Path(__file__).parent.parent / "inputs" / f"day_{day:02d}.txt"
    with open(input_path, 'r') as f:
        return f.read()


def read_lines(day: int, strip: bool = True) -> List[str]:
    """Read input file as a list of lines.

    Args:
        day: The day number (1-25)
        strip: Whether to strip whitespace from each line

    Returns:
        List of lines from the input file
    """
    content = read_input(day)
    lines = content.splitlines()
    return [line.strip() if strip else line for line in lines]


def read_blocks(day: int) -> List[str]:
    """Read input file as blocks separated by blank lines.

    Args:
        day: The day number (1-25)

    Returns:
        List of text blocks
    """
    content = read_input(day)
    return content.split('\n\n')


def read_grid(day: int) -> List[List[str]]:
    """Read input file as a 2D grid of characters.

    Args:
        day: The day number (1-25)

    Returns:
        2D list representing the grid
    """
    lines = read_lines(day)
    return [list(line) for line in lines]


def read_int_grid(day: int) -> List[List[int]]:
    """Read input file as a 2D grid of integers.

    Args:
        day: The day number (1-25)

    Returns:
        2D list of integers
    """
    lines = read_lines(day)
    return [[int(char) for char in line] for line in lines]
