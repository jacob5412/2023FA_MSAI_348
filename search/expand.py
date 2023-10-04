"""
Defines an expand function to expand child nodes during tree traversal.
"""


def expand(node, _map):
    """
    Expands child nodes of a parent node during tree traversal.

    Args:
        node (str): The current node to expand.
        _map (dict): A dictionary representing the adjacency map of the tree.

    Returns:
        list: A list of child nodes that are not None in the adjacency map.
    """
    expand_count = expand_count + 1
    return [next for next in _map[node] if _map[node][next] is not None]
