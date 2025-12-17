#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 10: Factory

Solve "Lights Out" puzzle using Gaussian elimination over GF(2).
"""

import sys
from pathlib import Path
import re

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def parse_input(data: str):
    """Parse the input data into machines."""
    machines = []
    lines = data.strip().split('\n')

    for line in lines:
        # Extract indicator lights pattern
        light_match = re.search(r'\[([.#]+)\]', line)
        lights = light_match.group(1)

        # Extract button configurations
        buttons = []
        for button_match in re.finditer(r'\(([0-9,]+)\)', line):
            button_lights = [int(x) for x in button_match.group(1).split(',')]
            buttons.append(button_lights)

        # Extract joltage requirements
        joltage_match = re.search(r'\{([0-9,]+)\}', line)
        joltages = [int(x) for x in joltage_match.group(1).split(',')]

        machines.append({
            'target': lights,
            'buttons': buttons,
            'joltages': joltages
        })

    return machines


def solve_lights_out(target, buttons):
    """
    Solve the lights out puzzle using Gaussian elimination over GF(2).
    Returns the minimum number of button presses, or None if impossible.
    """
    n_lights = len(target)
    n_buttons = len(buttons)

    # Convert target to binary (0 = off, 1 = on)
    target_state = [1 if c == '#' else 0 for c in target]

    # Build augmented matrix for Gaussian elimination
    matrix = []
    for light_idx in range(n_lights):
        row = [0] * (n_buttons + 1)
        for button_idx, button in enumerate(buttons):
            if light_idx in button:
                row[button_idx] = 1
        row[n_buttons] = target_state[light_idx]
        matrix.append(row)

    # Gaussian elimination to reduced row echelon form
    pivot_cols = []
    current_row = 0

    for col in range(n_buttons):
        # Find pivot
        pivot_row = None
        for row in range(current_row, n_lights):
            if matrix[row][col] == 1:
                pivot_row = row
                break

        if pivot_row is None:
            continue

        # Swap rows
        if pivot_row != current_row:
            matrix[current_row], matrix[pivot_row] = matrix[pivot_row], matrix[current_row]

        pivot_cols.append(col)

        # Eliminate all other rows
        for row in range(n_lights):
            if row != current_row and matrix[row][col] == 1:
                for c in range(n_buttons + 1):
                    matrix[row][c] ^= matrix[current_row][c]

        current_row += 1

    # Check for contradictions
    for row in range(current_row, n_lights):
        if matrix[row][n_buttons] == 1:
            return None  # No solution

    # Find free variables (columns not in pivot_cols)
    free_vars = [col for col in range(n_buttons) if col not in pivot_cols]

    # If no free variables, there's only one solution
    if not free_vars:
        solution = [0] * n_buttons
        for i, col in enumerate(pivot_cols):
            solution[col] = matrix[i][n_buttons]
        return sum(solution)

    # Enumerate all combinations of free variables to find minimum
    min_presses = float('inf')

    for mask in range(1 << len(free_vars)):
        solution = [0] * n_buttons

        # Set free variables according to mask
        for i, var in enumerate(free_vars):
            solution[var] = (mask >> i) & 1

        # Determine dependent variables
        for i, col in enumerate(pivot_cols):
            val = matrix[i][n_buttons]
            for j in range(col + 1, n_buttons):
                val ^= (matrix[i][j] & solution[j])
            solution[col] = val

        # Count button presses
        presses = sum(solution)
        min_presses = min(min_presses, presses)

    return min_presses if min_presses != float('inf') else None


def part1(machines):
    """Find the minimum button presses for all machines."""
    total = 0
    for machine in machines:
        min_presses = solve_lights_out(machine['target'], machine['buttons'])
        if min_presses is None:
            return None  # Should not happen with valid input
        total += min_presses
    return total


def solve_joltage(targets, buttons):
    """
    Solve the joltage configuration problem using integer linear programming.
    Returns the minimum number of button presses to reach target joltage levels.
    """
    from scipy.optimize import linprog
    import numpy as np

    n_counters = len(targets)
    n_buttons = len(buttons)

    # Build constraint matrix: A_eq * x = b_eq
    # Each row represents a counter, each column represents a button
    A_eq = np.zeros((n_counters, n_buttons))
    for button_idx, button in enumerate(buttons):
        for counter_idx in button:
            A_eq[counter_idx, button_idx] = 1

    b_eq = np.array(targets, dtype=float)

    # Objective: minimize sum of button presses
    c = np.ones(n_buttons)

    # Bounds: each button can be pressed 0 or more times
    bounds = [(0, None) for _ in range(n_buttons)]

    # Solve using linear programming with integer constraints
    result = linprog(
        c,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method='highs',
        integrality=[1] * n_buttons  # All variables must be integers
    )

    if result.success:
        return int(round(result.fun))
    else:
        return None


def part2(machines):
    """Find the minimum button presses for joltage configuration."""
    total = 0
    for machine in machines:
        min_presses = solve_joltage(machine['joltages'], machine['buttons'])
        if min_presses is None:
            return None  # Should not happen with valid input
        total += min_presses
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
