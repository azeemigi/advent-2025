#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 8: Playground

Connect junction boxes using Union-Find to track circuits.
"""

import sys
from pathlib import Path
import math
from collections import Counter

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input, read_lines


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure."""
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """Find the root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in the same set
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True  # Successfully merged
    
    def get_component_sizes(self):
        """Get the sizes of all connected components."""
        components = Counter()
        for i in range(len(self.parent)):
            root = self.find(i)
            components[root] += 1
        return list(components.values())


def parse_input(data: str):
    """Parse the input data into 3D coordinates."""
    lines = data.strip().split('\n')
    positions = []
    for line in lines:
        x, y, z = map(int, line.split(','))
        positions.append((x, y, z))
    return positions


def distance(p1, p2):
    """Calculate Euclidean distance between two 3D points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


def part1(positions):
    """Connect the 1000 closest pairs and find product of three largest circuits."""
    n = len(positions)
    
    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(positions[i], positions[j])
            distances.append((dist, i, j))
    
    # Sort by distance
    distances.sort()
    
    # Use Union-Find to track circuits
    uf = UnionFind(n)
    
    # Connect the 1000 closest pairs
    for i in range(min(1000, len(distances))):
        dist, box1, box2 = distances[i]
        uf.union(box1, box2)
    
    # Get sizes of all circuits
    circuit_sizes = uf.get_component_sizes()
    
    # Sort to get the three largest
    circuit_sizes.sort(reverse=True)
    
    # Multiply the three largest
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


def part2(positions):
    """Connect pairs until all junction boxes are in one circuit."""
    n = len(positions)
    
    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(positions[i], positions[j])
            distances.append((dist, i, j))
    
    # Sort by distance
    distances.sort()
    
    # Use Union-Find to track circuits
    uf = UnionFind(n)
    
    # Keep connecting until all are in one circuit
    for dist, box1, box2 in distances:
        # Try to connect these boxes
        connected = uf.union(box1, box2)
        
        if connected:
            # Check if all are now in one circuit
            component_sizes = uf.get_component_sizes()
            if len(component_sizes) == 1:
                # All in one circuit - this was the last connection
                x1 = positions[box1][0]
                x2 = positions[box2][0]
                return x1 * x2
    
    return None


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
