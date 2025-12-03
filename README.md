# Advent of Code 2025

Python solutions for [Advent of Code 2025](https://adventofcode.com/2025).

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
- `inputs/day_XX.txt` - Empty input file (manually paste your input)

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

| Day | Part 1 | Part 2 |
|-----|--------|--------|
| 1   | ⭐     | ⭐     |
| 2   |        |        |
| ... |        |        |
