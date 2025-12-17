#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 6: Trash Compactor

Solve cephalopod math problems arranged vertically in columns.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def parse_input(data: str):
    """Parse the vertically-arranged math problems.

    Returns:
        List of problems, where each problem is a tuple of (numbers, operation)
    """
    lines = data.strip().split('\n')

    # Find the width of the worksheet
    max_width = max(len(line) for line in lines)

    # Pad all lines to same width
    padded_lines = [line.ljust(max_width) for line in lines]

    problems = []
    col = 0

    while col < max_width:
        # Skip blank columns
        if all(line[col] == ' ' for line in padded_lines):
            col += 1
            continue

        # Found start of a problem - collect all columns until next blank
        problem_cols = []
        while col < max_width and not all(line[col] == ' ' for line in padded_lines):
            problem_cols.append(col)
            col += 1

        # Extract the problem from these columns
        numbers = []
        operation = None

        for line in padded_lines:
            # Get text from this problem's columns
            text = ''.join(line[c] for c in problem_cols).strip()

            if text:
                if text in ['+', '*']:
                    operation = text
                else:
                    numbers.append(int(text))

        if numbers and operation:
            problems.append((numbers, operation))

    return problems


def solve_problem(numbers, operation):
    """Solve a single math problem.

    Args:
        numbers: List of numbers to operate on
        operation: '+' or '*'

    Returns:
        Result of the operation
    """
    if operation == '+':
        return sum(numbers)
    else:  # operation == '*'
        result = 1
        for num in numbers:
            result *= num
        return result


def part1(problems):
    """Calculate the grand total of all problem answers."""
    grand_total = 0

    for numbers, operation in problems:
        answer = solve_problem(numbers, operation)
        grand_total += answer

    return grand_total


def parse_input_rtl(data: str):
    """Parse the vertically-arranged math problems reading right-to-left.

    In cephalopod math, problems are read RTL. Within each problem, each COLUMN
    represents ONE number, with digits stacked vertically (most significant at top).

    Returns:
        List of problems, where each problem is a tuple of (numbers, operation)
    """
    lines = data.strip().split('\n')

    # Find the width of the worksheet
    max_width = max(len(line) for line in lines)

    # Pad all lines to same width
    padded_lines = [line.ljust(max_width) for line in lines]

    problems = []
    col = 0

    while col < max_width:
        # Skip blank columns
        if all(line[col] == ' ' for line in padded_lines):
            col += 1
            continue

        # Found start of a problem - collect all columns until next blank
        problem_start = col
        while col < max_width and not all(line[col] == ' ' for line in padded_lines):
            col += 1
        problem_end = col

        # Extract operation from last row
        operation = None
        for c in range(problem_start, problem_end):
            char = padded_lines[-1][c]
            if char in ['+', '*']:
                operation = char
                break

        # Each column in the problem (reading RTL) represents ONE number
        # Digits are stacked vertically within that column (top = most significant)
        numbers = []
        num_rows = len(padded_lines) - 1  # Exclude operation row

        # Process columns from right to left
        for c in range(problem_end - 1, problem_start - 1, -1):
            # Collect digits from this column, top to bottom
            digits = []
            for row_idx in range(num_rows):
                char = padded_lines[row_idx][c]
                if char.isdigit():
                    digits.append(char)

            if digits:
                # Digits are already in correct order (top to bottom = most to least significant)
                number = int(''.join(digits))
                numbers.append(number)

        if numbers and operation:
            problems.append((numbers, operation))

    return problems


def part2(problems_part1):
    """Calculate the grand total using right-to-left cephalopod math."""
    # Re-parse the original input with right-to-left reading
    from pathlib import Path
    day = 6
    input_path = Path(__file__).parent.parent / "inputs" / f"day_{day:02d}.txt"
    with open(input_path, 'r') as f:
        data = f.read()

    problems = parse_input_rtl(data)

    grand_total = 0
    for numbers, operation in problems:
        answer = solve_problem(numbers, operation)
        grand_total += answer

    return grand_total


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
