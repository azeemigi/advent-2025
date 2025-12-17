#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 5: Cafeteria

Determine which available ingredient IDs are fresh based on ID ranges.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def parse_input(data: str):
    """Parse the input data into ranges and available IDs.

    Returns:
        Tuple of (ranges, available_ids) where ranges is a list of (min, max) tuples
        and available_ids is a list of integers.
    """
    blocks = data.strip().split('\n\n')

    # Parse ranges
    ranges = []
    for line in blocks[0].strip().split('\n'):
        start, end = line.split('-')
        ranges.append((int(start), int(end)))

    # Parse available IDs
    available_ids = [int(line) for line in blocks[1].strip().split('\n')]

    return ranges, available_ids


def is_fresh(ingredient_id, ranges):
    """Check if an ingredient ID is fresh (falls into any range).

    Args:
        ingredient_id: The ID to check
        ranges: List of (min, max) tuples representing fresh ranges

    Returns:
        True if the ID is in any range, False otherwise
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def part1(data):
    """Count how many available ingredient IDs are fresh."""
    ranges, available_ids = data

    fresh_count = 0
    for ingredient_id in available_ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1

    return fresh_count


def part2(data):
    """Count total ingredient IDs considered fresh by the ranges.

    Find the union of all ranges and count how many IDs are covered.
    """
    ranges, _ = data  # We don't need the available IDs for part 2

    if not ranges:
        return 0

    # Sort ranges by start position
    sorted_ranges = sorted(ranges)

    # Merge overlapping ranges
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # If current range overlaps or is adjacent to the last merged range
        if start <= last_end + 1:
            # Merge by extending the end if needed
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged.append((start, end))

    # Count total IDs in merged ranges
    total = 0
    for start, end in merged:
        total += end - start + 1

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
