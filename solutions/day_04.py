#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 4: Printing Department

Find how many paper rolls can be accessed by forklifts.
A roll is accessible if it has fewer than 4 neighboring rolls in the 8 adjacent positions.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input, read_lines
from utils.grid import DIRECTIONS_8


def parse_input(data: str):
    """Parse the input data into a 2D grid."""
    lines = data.strip().split('\n')
    return [list(line) for line in lines]


def count_adjacent_rolls(grid, row, col):
    """Count the number of paper rolls in the 8 adjacent positions.
    
    Args:
        grid: The 2D grid
        row: Current row
        col: Current column
        
    Returns:
        Number of adjacent paper rolls (0-8)
    """
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for dr, dc in DIRECTIONS_8:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    
    return count


def part1(grid):
    """Count how many rolls can be accessed by forklifts.
    
    A roll can be accessed if it has fewer than 4 adjacent rolls.
    """
    accessible_count = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Only check positions that have a paper roll
            if grid[row][col] == '@':
                adjacent_rolls = count_adjacent_rolls(grid, row, col)
                if adjacent_rolls < 4:
                    accessible_count += 1
    
    return accessible_count


def part2(grid):
    """Count total rolls that can be removed through iterative process.
    
    Keep removing accessible rolls (those with < 4 neighbors) until
    no more rolls can be removed.
    """
    # Make a copy of the grid so we don't modify the original
    grid = [row[:] for row in grid]
    total_removed = 0
    
    while True:
        # Find all accessible rolls in current state
        accessible = []
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '@':
                    adjacent_rolls = count_adjacent_rolls(grid, row, col)
                    if adjacent_rolls < 4:
                        accessible.append((row, col))
        
        # If no more accessible rolls, we're done
        if not accessible:
            break
        
        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = '.'
        
        total_removed += len(accessible)
    
    return total_removed


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
