#!/usr/bin/env python3
"""
Advent of Code 2025 - Day XX
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input, read_lines


def parse_input(data: str):
    """Parse the input data."""
    # TODO: Implement parsing logic
    lines = data.strip().split('\n')
    return lines


def part1(data):
    """Solve part 1."""
    # TODO: Implement part 1 solution
    return None


def part2(data):
    """Solve part 2."""
    # TODO: Implement part 2 solution
    return None


def main():
    # Get day number from filename
    day = int(Path(__file__).stem.split('_')[1])
    
    # Read and parse input
    raw_input = read_input(day)
    data = parse_input(raw_input)
    
    # Solve and print results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
