#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 3: Lobby

Find the maximum joltage possible from each battery bank by selecting
exactly 2 batteries (keeping their order).
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def parse_input(data: str):
    """Parse the input data into list of battery banks."""
    return data.strip().split('\n')


def max_joltage_from_bank(bank: str) -> int:
    """Find the maximum joltage from a battery bank.

    Select exactly 2 batteries (in order) to form the largest 2-digit number.

    Args:
        bank: String of digits representing battery joltages

    Returns:
        Maximum joltage (2-digit number) possible from this bank
    """
    max_joltage = 0

    # Try all pairs of batteries (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form a 2-digit number from batteries at positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)

    return max_joltage


def part1(banks):
    """Find the total output joltage from all banks."""
    total = 0

    for bank in banks:
        max_joltage = max_joltage_from_bank(bank)
        total += max_joltage

    return total


def max_joltage_from_bank_n(bank: str, n: int) -> int:
    """Find the maximum joltage from a battery bank by selecting n batteries.

    To maximize the n-digit number, we need to greedily select batteries:
    - For each position in our result (left to right), choose the largest digit
      that still leaves enough batteries remaining to fill the rest.

    Args:
        bank: String of digits representing battery joltages
        n: Number of batteries to select

    Returns:
        Maximum joltage (n-digit number) possible from this bank
    """
    result = []
    start_idx = 0

    for position in range(n):
        # How many more batteries do we need after this position?
        remaining_needed = n - position - 1

        # Latest index we can start from and still have enough batteries left
        latest_start = len(bank) - remaining_needed - 1

        # Find the maximum digit in the valid range
        max_digit = '0'
        max_idx = start_idx

        for i in range(start_idx, latest_start + 1):
            if bank[i] > max_digit:
                max_digit = bank[i]
                max_idx = i

        result.append(max_digit)
        start_idx = max_idx + 1

    return int(''.join(result))


def part2(banks):
    """Find the total output joltage by selecting exactly 12 batteries per bank."""
    total = 0

    for bank in banks:
        max_joltage = max_joltage_from_bank_n(bank, 12)
        total += max_joltage

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
