#!/usr/bin/env python3
"""Test Day 10 with the example."""

from solutions.day_10 import parse_input, part1, part2, solve_lights_out, solve_joltage

example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

machines = parse_input(example)

# Test Part 1
result_part1 = part1(machines)
print(f"Part 1 test result: {result_part1} (expected: 7)")

# Test individual machines for Part 1
print("\nPart 1 - Individual machine results:")
for i, machine in enumerate(machines):
    min_presses = solve_lights_out(machine['target'], machine['buttons'])
    print(f"  Machine {i+1}: {min_presses} button presses")

# Test Part 2
result_part2 = part2(machines)
print(f"\nPart 2 test result: {result_part2} (expected: 33)")

# Test individual machines for Part 2
print("\nPart 2 - Individual machine results:")
for i, machine in enumerate(machines):
    min_presses = solve_joltage(machine['joltages'], machine['buttons'])
    print(f"  Machine {i+1}: {min_presses} button presses")
