"""
Implementation of DFS.
"""

from data_utils import LIFOQueue
from expand import expand


def depth_first_search(time_map, start, end):
    """
    Performs Depth-First Search (DFS) algorithm to find the path
    from start to end.

    Args:
        time_map (dict): A dictionary containing the similarity map.
        start (str): The starting node.
        end (str): The goal node.

    Returns:
        list or None: The path from start to end, or None if no path is found.
    """
    frontier = LIFOQueue()
    frontier.push(start, [start])
    while not frontier.is_empty():
        current_node, path = frontier.pop()
        if current_node == end:
            return path
        for child_node in expand(current_node, time_map):
            if not frontier.is_exists(child_node):
                new_path = path + [child_node]
                frontier.push(child_node, new_path)
    return None
