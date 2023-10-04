"""
Implementation of A*.
"""

from data_utils import PriorityQueue, Set
from expand import expand


def a_star_search(dis_map, time_map, start, end):
    """
    Performs A* search algorithm to find the path from start to end.

    Args:
        dis_map (dict): A dictionary containing the distance map.
        time_map (dict): A dictionary containing the similarity map.
        start (str): The starting node.
        end (str): The goal node.

    Returns:
        list or None: The shortest path from start to end, or None if no path
                      is found.
    """
    frontier = PriorityQueue()
    explored_set = Set()
    frontier.enqueue(start, [start], 0, dis_map[start][end])
    g_n_scores = {}
    f_n_scores = {}
    g_n_scores[start] = 0
    f_n_scores[start] = dis_map[start][end]
    while not frontier.is_empty():
        current_node, path = frontier.dequeue()
        if current_node == end:
            return path
        _ = explored_set.enqueue(current_node)
        for neighbor in expand(current_node, time_map):
            if explored_set.is_exists(neighbor):
                continue
            new_g_n_score = g_n_scores[current_node] + time_map[current_node][neighbor]
            # not in frontier and the new g_n_score is lower
            if (
                not frontier.is_exists(neighbor)
                or new_g_n_score <= g_n_scores[neighbor]
            ):
                g_n_scores[neighbor] = new_g_n_score
                h_n_score = dis_map[neighbor][end]
                f_n_scores[neighbor] = new_g_n_score + h_n_score
                new_path = path + [neighbor]
                frontier.enqueue(neighbor, new_path, f_n_scores[neighbor], h_n_score)
    return None
