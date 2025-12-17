#!/usr/bin/env python3
"""
Run all Advent of Code 2025 solutions.

This script executes all implemented daily solutions and displays
their results in a formatted table.
"""

import sys
import time
from pathlib import Path
from importlib import import_module


# Problem descriptions for each day
DESCRIPTIONS = {
    1: "Secret Entrance - Safe dial rotations",
    2: "Gift Shop - Invalid product IDs",
    3: "Lobby - Battery joltage optimization",
    4: "Printing Department - Paper roll access",
    5: "Cafeteria - Fresh ingredient ID ranges",
    6: "Trash Compactor - Cephalopod math",
    7: "Laboratories - Tachyon beam splitting",
    8: "Playground - Junction box circuits",
    9: "Movie Theater - Largest rectangle",
    10: "Factory - Lights Out & Joltage",
}


def run_day(day: int):
    """Run a single day's solution and return results."""
    try:
        # Import the day's module
        module = import_module(f'solutions.day_{day:02d}')

        # Read the input
        input_file = Path(f'inputs/day_{day:02d}.txt')
        if not input_file.exists():
            return None, None, "Input file not found"

        raw_input = input_file.read_text()

        # Parse and solve
        start_time = time.time()
        data = module.parse_input(raw_input)
        part1_result = module.part1(data)
        part2_result = module.part2(data)
        elapsed = time.time() - start_time

        return part1_result, part2_result, f"{elapsed:.3f}s"

    except ImportError:
        return None, None, "Not implemented"
    except Exception as e:
        return None, None, f"Error: {str(e)[:30]}"


def main():
    """Run all solutions and display results."""
    print("=" * 80)
    print("Advent of Code 2025 - All Solutions".center(80))
    print("=" * 80)
    print()

    # Table header
    print(f"{'Day':<5} {'Description':<35} {'Part 1':<15} {'Part 2':<15} {'Time':<10}")
    print("-" * 80)

    total_stars = 0
    total_time = 0.0

    # Run each day
    for day in range(1, 26):
        if day not in DESCRIPTIONS:
            continue

        part1, part2, time_str = run_day(day)

        # Count stars
        if part1 is not None:
            total_stars += 1
        if part2 is not None:
            total_stars += 1

        # Format results
        p1_str = str(part1) if part1 is not None else "-"
        p2_str = str(part2) if part2 is not None else "-"

        # Truncate long results
        if len(p1_str) > 13:
            p1_str = p1_str[:10] + "..."
        if len(p2_str) > 13:
            p2_str = p2_str[:10] + "..."

        # Extract time if available
        if time_str.endswith('s'):
            try:
                total_time += float(time_str[:-1])
            except ValueError:
                pass

        print(f"{day:<5} {DESCRIPTIONS[day]:<35} {p1_str:<15} {p2_str:<15} {time_str:<10}")

    # Summary
    print("-" * 80)
    print(f"\nTotal Stars: {total_stars} ⭐")
    print(f"Total Time: {total_time:.3f}s")
    print()


if __name__ == "__main__":
    main()
