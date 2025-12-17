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

### Run a solution:
```bash
python solutions/day_01.py
```

## Project Structure

```
advent-2025/
├── solutions/       # Daily solution files
├── inputs/          # Puzzle inputs
├── utils/           # Helper utilities
├── setup_day.py     # Script to generate new day files
└── requirements.txt # Python dependencies
```

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