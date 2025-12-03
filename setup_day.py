#!/usr/bin/env python3
"""
Script to set up files for a new Advent of Code day.
Usage: python setup_day.py <day_number>
"""

import sys
from pathlib import Path
import shutil


def setup_day(day: int):
    """Create solution and input files for a given day.
    
    Args:
        day: Day number (1-25)
    """
    if not 1 <= day <= 25:
        print(f"Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)
    
    base_dir = Path(__file__).parent
    
    # Create solution file from template
    solution_file = base_dir / "solutions" / f"day_{day:02d}.py"
    if solution_file.exists():
        print(f"Warning: {solution_file} already exists, skipping...")
    else:
        template_file = base_dir / "template.py"
        shutil.copy(template_file, solution_file)
        print(f"✓ Created {solution_file}")
    
    # Create empty input file
    input_file = base_dir / "inputs" / f"day_{day:02d}.txt"
    if input_file.exists():
        print(f"Warning: {input_file} already exists, skipping...")
    else:
        input_file.touch()
        print(f"✓ Created {input_file}")
    
    print(f"\nDay {day} is ready! Next steps:")
    print(f"1. Paste your puzzle input into {input_file}")
    print(f"2. Implement your solution in {solution_file}")
    print(f"3. Run with: python {solution_file}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python setup_day.py <day_number>")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
    except ValueError:
        print(f"Error: Invalid day number '{sys.argv[1]}'")
        sys.exit(1)
    
    setup_day(day)


if __name__ == "__main__":
    main()
