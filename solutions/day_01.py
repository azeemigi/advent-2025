#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1: Secret Entrance

The safe has a dial with numbers 0-99. Follow rotation instructions (L/R + distance)
to find how many times the dial points at 0.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input, read_lines


def parse_input(data: str):
    """Parse the input data into a list of (direction, distance) tuples."""
    rotations = []
    for line in data.strip().split('\n'):
        direction = line[0]  # 'L' or 'R'
        distance = int(line[1:])  # The number after the direction
        rotations.append((direction, distance))
    return rotations


def part1(rotations):
    """Count how many times the dial points at 0 after any rotation."""
    position = 50  # Starting position
    count = 0
    
    for direction, distance in rotations:
        if direction == 'L':
            # Rotate left (toward lower numbers)
            position = (position - distance) % 100
        else:  # direction == 'R'
            # Rotate right (toward higher numbers)
            position = (position + distance) % 100
        
        # Check if we're at 0 after this rotation
        if position == 0:
            count += 1
    
    return count


def part2(rotations):
    """Count how many times the dial points at 0 during AND after rotations.
    
    This includes every click that causes the dial to point at 0, even during
    a rotation (not just at the end).
    """
    position = 50  # Starting position
    count = 0
    
    for direction, distance in rotations:
        # Count how many times we pass through 0 during this rotation
        if direction == 'L':
            # Moving left (decreasing position)
            for _ in range(distance):
                position = (position - 1) % 100
                if position == 0:
                    count += 1
        else:  # direction == 'R'
            # Moving right (increasing position)
            for _ in range(distance):
                position = (position + 1) % 100
                if position == 0:
                    count += 1
    
    return count


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
