"""Grid utility functions for Advent of Code."""

from typing import List, Tuple


# Common direction vectors
DIRECTIONS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
DIRECTIONS_8 = [
    (0, 1), (1, 1), (1, 0), (1, -1),
    (0, -1), (-1, -1), (-1, 0), (-1, 1)
]  # All 8 directions including diagonals

DIRECTION_NAMES = {
    (0, 1): 'E',
    (1, 0): 'S',
    (0, -1): 'W',
    (-1, 0): 'N',
}


def in_bounds(grid: List[List], row: int, col: int) -> bool:
    """Check if coordinates are within grid bounds.

    Args:
        grid: The grid to check
        row: Row index
        col: Column index

    Returns:
        True if coordinates are valid, False otherwise
    """
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def get_neighbors_4(row: int, col: int, max_row: int, max_col: int) -> List[Tuple[int, int]]:
    """Get 4-directional neighbors (no diagonals).

    Args:
        row: Current row
        col: Current column
        max_row: Maximum row index (exclusive)
        max_col: Maximum column index (exclusive)

    Returns:
        List of valid neighbor coordinates
    """
    neighbors = []
    for dr, dc in DIRECTIONS_4:
        nr, nc = row + dr, col + dc
        if 0 <= nr < max_row and 0 <= nc < max_col:
            neighbors.append((nr, nc))
    return neighbors


def get_neighbors_8(row: int, col: int, max_row: int, max_col: int) -> List[Tuple[int, int]]:
    """Get 8-directional neighbors (including diagonals).

    Args:
        row: Current row
        col: Current column
        max_row: Maximum row index (exclusive)
        max_col: Maximum column index (exclusive)

    Returns:
        List of valid neighbor coordinates
    """
    neighbors = []
    for dr, dc in DIRECTIONS_8:
        nr, nc = row + dr, col + dc
        if 0 <= nr < max_row and 0 <= nc < max_col:
            neighbors.append((nr, nc))
    return neighbors


def find_in_grid(grid: List[List[str]], target: str) -> List[Tuple[int, int]]:
    """Find all positions of a character in the grid.

    Args:
        grid: The grid to search
        target: The character to find

    Returns:
        List of (row, col) positions where target appears
    """
    positions = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == target:
                positions.append((r, c))
    return positions


def print_grid(grid: List[List]) -> None:
    """Print a grid in a readable format.

    Args:
        grid: The grid to print
    """
    for row in grid:
        print(''.join(str(cell) for cell in row))
