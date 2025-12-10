#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 7: Laboratories

Simulate tachyon beam splitting through a manifold and count total splits.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input, read_lines


def parse_input(data: str):
    """Parse the input data into a grid."""
    lines = data.strip().split('\n')
    return [list(line) for line in lines]


def find_start(grid):
    """Find the starting position marked with 'S'."""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return (r, c)
    return None


def simulate_beam(grid):
    """Simulate the tachyon beam and count splits.
    
    All beams move downward. When a beam hits a splitter (^), it stops and
    two new beams are created from the immediate left and right of the splitter,
    both moving downward.
    
    Returns:
        Number of times beams are split
    """
    rows = len(grid)
    cols = len(grid[0])
    
    start_pos = find_start(grid)
    if not start_pos:
        return 0
    
    # Track active beams: (row, col)
    # All beams always move downward
    from collections import deque
    beams = deque([start_pos])
    split_count = 0
    
    # Track which positions we've already processed to avoid infinite loops
    visited = set()
    
    while beams:
        row, col = beams.popleft()
        
        # Skip if we've already processed this position
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        # Move the beam one step down
        next_row = row + 1
        
        # Check if beam exits the grid
        if next_row >= rows:
            continue
        
        # Check what's at the next position
        cell = grid[next_row][col]
        
        if cell == '^':
            # Hit a splitter - this counts as ONE split event
            split_count += 1
            # Create two new beams from the left and right of the splitter
            # Both continue downward from their respective positions
            if col - 1 >= 0:
                beams.append((next_row, col - 1))
            if col + 1 < cols:
                beams.append((next_row, col + 1))
        else:
            # Empty space or 'S' - continue downward
            beams.append((next_row, col))
    
    return split_count


def part1(grid):
    """Count how many times the beam is split."""
    return simulate_beam(grid)


def count_timelines(grid):
    """Count the number of distinct timelines using many-worlds interpretation.
    
    Each time a particle hits a splitter, the timeline splits into two.
    We recursively count all possible paths through the grid.
    
    Returns:
        Number of distinct timelines
    """
    rows = len(grid)
    cols = len(grid[0])
    
    start_pos = find_start(grid)
    if not start_pos:
        return 0
    
    # Use memoization to avoid recalculating paths from the same position
    memo = {}
    
    def count_paths_from(row, col):
        """Count the number of distinct paths from this position to any exit."""
        if (row, col) in memo:
            return memo[(row, col)]
        
        # Try to move down
        next_row = row + 1
        
        # Check if exits the grid
        if next_row >= rows:
            # This path exits - count as 1 timeline
            return 1
        
        cell = grid[next_row][col]
        
        if cell == '^':
            # Hit a splitter - timeline splits into left and right paths
            left_count = 0
            right_count = 0
            
            if col - 1 >= 0:
                left_count = count_paths_from(next_row, col - 1)
            if col + 1 < cols:
                right_count = count_paths_from(next_row, col + 1)
            
            result = left_count + right_count
        else:
            # Empty space - continue down
            result = count_paths_from(next_row, col)
        
        memo[(row, col)] = result
        return result
    
    return count_paths_from(start_pos[0], start_pos[1])


def part2(grid):
    """Count the number of different timelines using quantum interpretation."""
    return count_timelines(grid)


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
