#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 2: Gift Shop

Find invalid product IDs (numbers that are a sequence of digits repeated twice)
in given ranges and sum them.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def parse_input(data: str):
    """Parse the input data into list of (start, end) range tuples."""
    # The input is a single line with comma-separated ranges
    ranges = []
    parts = data.strip().split(',')
    for part in parts:
        start, end = part.split('-')
        ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num: int) -> bool:
    """Check if a number is invalid (a sequence repeated exactly twice).

    Examples:
    - 11 -> "1" repeated twice = invalid
    - 6464 -> "64" repeated twice = invalid
    - 123123 -> "123" repeated twice = invalid
    - 101 -> not a simple repetition = valid
    """
    s = str(num)
    length = len(s)

    # Must be even length to split in half
    if length % 2 != 0:
        return False

    # Check if first half equals second half
    half = length // 2
    first_half = s[:half]
    second_half = s[half:]

    return first_half == second_half


def part1(ranges):
    """Find and sum all invalid IDs in the given ranges."""
    total = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num

    return total


def is_invalid_id_part2(num: int) -> bool:
    """Check if a number is invalid (a sequence repeated at least twice).

    Examples:
    - 11 -> "1" repeated 2 times = invalid
    - 111 -> "1" repeated 3 times = invalid
    - 6464 -> "64" repeated 2 times = invalid
    - 123123123 -> "123" repeated 3 times = invalid
    - 1212121212 -> "12" repeated 5 times = invalid
    """
    s = str(num)
    length = len(s)

    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the string is composed of this pattern repeated
        pattern = s[:pattern_len]

        # Check if the entire string can be made by repeating this pattern
        if length % pattern_len == 0:
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True

    return False


def part2(ranges):
    """Find and sum all invalid IDs using the new rules (repeated at least twice)."""
    total = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id_part2(num):
                total += num

    return total


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
