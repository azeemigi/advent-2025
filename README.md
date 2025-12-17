# Advent of Code 2025 - Solutions

My Python solutions for [Advent of Code 2025](https://adventofcode.com/2025).

> **Disclaimer**: This repository contains personal solutions to Advent of Code puzzles. Advent of Code is a registered trademark of Advent of Code. This project is not affiliated with, endorsed by, or sponsored by Advent of Code.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install flake8 autopep8 autoflake  # Optional: for linting and formatting
```

3. (Optional) Add your session cookie to `.env`:
```
AOC_SESSION=your_session_cookie_here
```

## Usage

### Generate a new day's solution files:
```bash
python setup_day.py <day_number>
```

This creates:
- `solutions/day_XX.py` - Solution template
- `inputs/day_XX.txt` - Empty input file (you must manually add your own puzzle input)

**Note**: Per [Advent of Code's copyright policy](https://adventofcode.com/about), puzzle inputs are not included in this repository. You must obtain your own inputs from the [Advent of Code website](https://adventofcode.com/2025).

### Run a single day's solution:
```bash
python solutions/day_01.py
```

### Run all solutions:
```bash
python run_all.py
```

This will execute all implemented solutions and display results in a formatted table with execution times.

### Check code quality:
```bash
flake8 solutions/ utils/
```

## Project Structure

```
advent-2025/
├── solutions/       # Daily solution files (day_01.py, day_02.py, ...)
├── inputs/          # Puzzle inputs (not tracked in git)
├── utils/           # Helper utilities
│   ├── __init__.py  # File I/O utilities (read_input, read_lines, read_blocks, read_grid)
│   ├── grid.py      # Grid utilities (DIRECTIONS, get_neighbors, find_in_grid)
│   └── algorithms.py # Common algorithms (BFS, Dijkstra, binary_search)
├── setup_day.py     # Script to generate new day files
├── run_all.py       # Execute all solutions at once
├── template.py      # Template for new solutions
├── .flake8          # Linting configuration
└── requirements.txt # Python dependencies
```

## Utilities

The `utils/` package provides helpful functions for common Advent of Code tasks:

- **File I/O**: `read_input()`, `read_lines()`, `read_blocks()`, `read_grid()`
- **Grid Navigation**: `DIRECTIONS_4`, `DIRECTIONS_8`, `get_neighbors()`, `find_in_grid()`
- **Algorithms**: `bfs()`, `dijkstra()`, `binary_search()`

## Progress

| Day | Part 1 | Part 2 | Notes |
|-----|--------|--------|-------|
| 1   | ⭐     | ⭐     | Secret Entrance - Safe dial rotations |
| 2   | ⭐     | ⭐     | Gift Shop - Invalid product IDs |
| 3   | ⭐     | ⭐     | Lobby - Battery joltage optimization |
| 4   | ⭐     | ⭐     | Printing Department - Paper roll access |
| 5   | ⭐     | ⭐     | Cafeteria - Fresh ingredient ID ranges |
| 6   | ⭐     | ⭐     | Trash Compactor - Cephalopod math |
| 7   | ⭐     | ⭐     | Laboratories - Tachyon beam splitting |
| 8   | ⭐     | ⭐     | Playground - Junction box circuits (Union-Find) |
| 9   | ⭐     | ⭐     | Movie Theater - Largest rectangle (coordinate compression) |
| 10  | ⭐     | ⭐     | Factory - Lights Out (GF(2)) & Joltage (ILP) |
| ... |        |        | |

**Total Stars: 20 ⭐**
## Legal

Advent of Code® is a registered trademark in the United States. This repository is not affiliated with, endorsed by, or sponsored by Advent of Code. All puzzle content, concepts, and design elements are © 2015-2025 Advent of Code, all rights reserved. 

This repository contains only personal solution implementations, which are not claimed by Advent of Code per their [legal statement](https://adventofcode.com/about).