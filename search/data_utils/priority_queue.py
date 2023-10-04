"""
Utilities module consisting of PriorityQueue
"""

from .nodes import PriorityQueueNode


class PriorityQueue:
    """
    Represents a Priority Queue using a class-based linked list. Note that
    priority here is the distance to the goal (heuristic), so the lower
    priority node should be dequeued first.

    Attributes:
        head: Reference to the first node (with the highest priority)
              order in the queue.
    """

    def __init__(self):
        """
        Initializes an empty PriorityQueue.
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.head is None

    def enqueue(self, data, path, priority, tiebreaking_priority=None):
        """
        Enqueues (adds) an element to the queue and placed it based on
        its priority. If element exists, update its attributes.

        Args:
            data: The data to be enqueued.
            path: Path until the node.
            priority: The priority associated with this data.
            tiebreaking_priority: Tie-breaking priority associated.
        """
        new_node = PriorityQueueNode(data, path, priority, tiebreaking_priority)
        if self._is_exists_and_update(data, path):
            pass
        else:
            if self.is_empty() or priority < self.head.get_priority():
                new_node.next = self.head
                self.head = new_node
            elif (
                priority == self.head.get_priority()
                and tiebreaking_priority < self.head.get_tiebreaking_priority()
            ):
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while current.get_next() and priority >= current.next.get_priority():
                    if (
                        priority == current.next.get_priority()
                        and tiebreaking_priority
                        < current.next.get_tiebreaking_priority()
                    ):
                        break
                    current = current.get_next()
                new_node.next = current.get_next()
                current.next = new_node

    def dequeue(self):
        """
        Dequeues (removes and returns) an element from the front of the queue.

        Returns:
            data: The data dequeued from the front of the queue.

        Raises:
            IndexError: If the queue is empty when dequeue is called.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.head.get_data()
        path = self.head.get_path()
        self.head = self.head.get_next()
        return data, path

    def is_exists(self, data):
        """
        Checks if a given element exists in the Queue.

        Args:
            data: The element to check for existence in the Queue.

        Returns:
            bool: True if the element exists in the Queue, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.get_next()
        return False

    def _is_exists_and_update(self, data, path):
        """
        Checks if a given element exists in the Queue and updates
        its path attribute.

        Args:
            data: The element to check for existence in the Queue.
            path: Attribute to update.

        Returns:
            bool: True if the element exists in the Queue, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                current.path = path
                return True
            current = current.get_next()
        return False
