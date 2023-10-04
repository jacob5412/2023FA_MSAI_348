"""
Utilities module consisting of nodes used in Queue
"""


class QueueNode:
    """
    Represents a node in a class-based linked list for a FIFO and a LIFO queue.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.
        path: Path associated with this node. The path discovered until this
              node in the search algorithm.
    """

    def __init__(self, data, path):
        self.data = data
        self.next = None
        self.path = path

    def get_data(self):
        """
        Gets the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.data

    def get_next(self):
        """
        Gets the reference to the next node in the linked list.

        Returns:
            The reference to the next node.
        """
        return self.next

    def get_path(self):
        """
        Gets the path associated with the node.

        Returns:
            The path stored in the node.
        """
        return self.path


class PriorityQueueNode:
    """
    Represents a node in a class-based linked list for a Prority queue.

    Attributes:
        data: The data stored in the node.
        path: Path associated with this node. The path discovered until this
              node in the search algorithm.
        priority: Priority associated with this node.
        tiebreaking_priority: Tie-breaking Priority associated with this node.
        next: Reference to the next node in the linked list.
    """

    def __init__(self, data, path, priority, tiebreaking_priority=None):
        self.data = data
        self.path = path
        self.priority = priority
        self.tiebreaking_priority = tiebreaking_priority
        self.next = None

    def get_data(self):
        """
        Gets the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.data

    def get_next(self):
        """
        Gets the reference to the next node in the linked list.

        Returns:
            The reference to the next node.
        """
        return self.next

    def get_priority(self):
        """
        Gets the priority associated with the node.

        Returns:
            The priority stored in the node.
        """
        return self.priority

    def get_tiebreaking_priority(self):
        """
        Gets the tie-breaking priority associated with the node.

        Returns:
            The tie-breaking priority stored in the node.
        """
        return self.tiebreaking_priority

    def get_path(self):
        """
        Gets the path associated with the node.

        Returns:
            The path stored in the node.
        """
        return self.path
