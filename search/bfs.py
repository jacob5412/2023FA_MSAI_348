"""
Implementation of BFS.
"""

from data_utils import FIFOQueue, Set
from expand import expand


def breadth_first_search(time_map, start, end):
    """
    Performs Breadth-First Search (BFS) algorithm to find the path
    from start to end.

    Args:
        time_map (dict): A dictionary containing the similarity map.
        start (str): The starting node.
        end (str): The goal node.

    Returns:
        list or None: The path from start to end, or None if no path is found.
    """
    frontier = FIFOQueue()
    frontier.enqueue(start, [start])
    explored_set = Set()
    while not frontier.is_empty():
        current_node, path = frontier.dequeue()
        _ = explored_set.enqueue(current_node)
        if current_node == end:
            return path
        for child_node in expand(current_node, time_map):
            if not frontier.is_exists(child_node) and not explored_set.is_exists(
                child_node
            ):
                new_path = path + [child_node]
                frontier.enqueue(child_node, new_path)
    return None
