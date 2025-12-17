"""Algorithm utility functions for Advent of Code."""

from collections import deque
from typing import Callable, Tuple, Optional, Any
from heapq import heappush, heappop


def bfs(start, is_goal: Callable, get_neighbors: Callable) -> Optional[Any]:
    """Generic breadth-first search.

    Args:
        start: Starting state
        is_goal: Function that returns True if state is the goal
        get_neighbors: Function that returns list of neighbor states

    Returns:
        The goal state if found, None otherwise
    """
    queue = deque([start])
    visited = {start}

    while queue:
        state = queue.popleft()

        if is_goal(state):
            return state

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return None


def bfs_distance(start, is_goal: Callable, get_neighbors: Callable) -> Optional[int]:
    """BFS that returns the distance to the goal.

    Args:
        start: Starting state
        is_goal: Function that returns True if state is the goal
        get_neighbors: Function that returns list of neighbor states

    Returns:
        Distance to goal if found, None otherwise
    """
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, dist = queue.popleft()

        if is_goal(state):
            return dist

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return None


def dijkstra(start, is_goal: Callable, get_neighbors: Callable) -> Optional[Tuple[int, Any]]:
    """Dijkstra's algorithm for weighted shortest path.

    Args:
        start: Starting state
        is_goal: Function that returns True if state is the goal
        get_neighbors: Function that returns list of (neighbor, cost) tuples

    Returns:
        Tuple of (total_cost, goal_state) if found, None otherwise
    """
    heap = [(0, start)]
    visited = set()

    while heap:
        cost, state = heappop(heap)

        if state in visited:
            continue

        visited.add(state)

        if is_goal(state):
            return cost, state

        for neighbor, edge_cost in get_neighbors(state):
            if neighbor not in visited:
                heappush(heap, (cost + edge_cost, neighbor))

    return None


def binary_search(predicate: Callable[[int], bool], low: int, high: int) -> int:
    """Binary search for the first value where predicate is True.

    Args:
        predicate: Function that returns True/False for a given value
        low: Lower bound (inclusive)
        high: Upper bound (inclusive)

    Returns:
        The smallest value where predicate is True
    """
    while low < high:
        mid = (low + high) // 2
        if predicate(mid):
            high = mid
        else:
            low = mid + 1
    return low
