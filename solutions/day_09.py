#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 9: Movie Theater

Find the largest rectangle using red tiles as opposite corners.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input


def parse_input(data: str):
    """Parse the input data into a list of red tile coordinates."""
    lines = data.strip().split('\n')
    tiles = []
    for line in lines:
        x, y = map(int, line.split(','))
        tiles.append((x, y))
    return tiles


def part1(tiles):
    """Find the largest rectangle area using two red tiles as opposite corners."""
    max_area = 0

    # Try all pairs of tiles as opposite corners
    n = len(tiles)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            # Calculate rectangle area (inclusive of both corners)
            # From x1 to x2 inclusive is |x2-x1|+1 tiles
            # From y1 to y2 inclusive is |y2-y1|+1 tiles
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height

            max_area = max(max_area, area)

    return max_area


def is_on_boundary(x, y, tiles):
    """Check if a point is on the boundary formed by consecutive red tiles."""
    n = len(tiles)
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]  # Wrap around

        # Check if (x, y) is on the line segment from (x1, y1) to (x2, y2)
        if x1 == x2:  # Vertical line
            if x == x1 and min(y1, y2) <= y <= max(y1, y2):
                return True
        elif y1 == y2:  # Horizontal line
            if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                return True

    return False


def is_inside_polygon(x, y, tiles):
    """Check if a point is inside the polygon using ray casting algorithm."""
    n = len(tiles)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = tiles[i]
        xj, yj = tiles[j]

        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside

        j = i

    return inside


def is_green_or_red(x, y, tiles, red_set):
    """Check if a tile is red or green."""
    # Check if it's a red tile
    if (x, y) in red_set:
        return True

    # Check if it's on the boundary
    if is_on_boundary(x, y, tiles):
        return True

    # Check if it's inside the polygon
    if is_inside_polygon(x, y, tiles):
        return True

    return False


def part2(tiles):
    """Find the largest rectangle using only red and green tiles."""
    n = len(tiles)

    # Coordinate compression
    xs = sorted(list(set(p[0] for p in tiles)))
    ys = sorted(list(set(p[1] for p in tiles)))

    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}

    W = len(xs) - 1
    H = len(ys) - 1

    # Build grid of elementary rectangles
    is_inside = [[False] * W for _ in range(H)]

    # Identify vertical edges for sweep line
    v_edges = []
    for k in range(n):
        p1 = tiles[k]
        p2 = tiles[(k + 1) % n]

        if p1[0] == p2[0]:  # Vertical edge
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            v_edges.append((p1[0], y_min, y_max))

    v_edges.sort()

    # Sweep line to mark interior cells
    for j in range(H):
        y_mid = (ys[j] + ys[j + 1]) / 2.0

        row_crossings = []
        for x, edge_ymin, edge_ymax in v_edges:
            if edge_ymin < y_mid < edge_ymax:
                row_crossings.append(x)

        row_crossings.sort()

        # Even-odd rule: regions between pairs are inside
        for k in range(0, len(row_crossings), 2):
            if k + 1 < len(row_crossings):
                x_start = row_crossings[k]
                x_end = row_crossings[k + 1]

                idx_start = x_map[x_start]
                idx_end = x_map[x_end]

                for i in range(idx_start, idx_end):
                    is_inside[j][i] = True

    # Build 2D prefix sum
    P = [[0] * (W + 1) for _ in range(H + 1)]
    for j in range(H):
        for i in range(W):
            val = 1 if is_inside[j][i] else 0
            P[j + 1][i + 1] = P[j][i + 1] + P[j + 1][i] - P[j][i] + val

    def count_valid_cells(ix1, iy1, ix2, iy2):
        if ix1 >= ix2 or iy1 >= iy2:
            return 0
        return P[iy2][ix2] - P[iy1][ix2] - P[iy2][ix1] + P[iy1][ix1]

    def is_point_inside(px, py):
        intersections = 0
        for k in range(n):
            p1 = tiles[k]
            p2 = tiles[(k + 1) % n]
            if p1[1] == p2[1]:
                continue

            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            if y_min <= py < y_max:
                x_int = p1[0] + (py - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                if px < x_int:
                    intersections += 1
        return (intersections % 2) == 1

    # Check all pairs
    max_area = 0
    for i in range(n):
        for k in range(i + 1, n):
            p1 = tiles[i]
            p2 = tiles[k]

            w = abs(p1[0] - p2[0]) + 1
            h = abs(p1[1] - p2[1]) + 1
            area = w * h

            if area <= max_area:
                continue

            # Check validity
            valid = False

            # Case: Aligned (1D)
            if p1[0] == p2[0] or p1[1] == p2[1]:
                mid_x = (p1[0] + p2[0]) / 2.0
                mid_y = (p1[1] + p2[1]) / 2.0

                if is_point_inside(mid_x, mid_y):
                    valid = True
                else:
                    # Check if on boundary
                    on_boundary = False
                    for e_idx in range(n):
                        ep1 = tiles[e_idx]
                        ep2 = tiles[(e_idx + 1) % n]
                        if ep1[1] == ep2[1] == mid_y:
                            if min(ep1[0], ep2[0]) <= mid_x <= max(ep1[0], ep2[0]):
                                on_boundary = True
                                break
                        elif ep1[0] == ep2[0] == mid_x:
                            if min(ep1[1], ep2[1]) <= mid_y <= max(ep1[1], ep2[1]):
                                on_boundary = True
                                break
                    if on_boundary:
                        valid = True

            # Case: 2D Rectangle
            else:
                idx_x1, idx_x2 = sorted((x_map[p1[0]], x_map[p2[0]]))
                idx_y1, idx_y2 = sorted((y_map[p1[1]], y_map[p2[1]]))

                expected_cells = (idx_x2 - idx_x1) * (idx_y2 - idx_y1)
                actual_cells = count_valid_cells(idx_x1, idx_y1, idx_x2, idx_y2)

                if actual_cells == expected_cells:
                    valid = True

            if valid:
                max_area = area

    return max_area


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
