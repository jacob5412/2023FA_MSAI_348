"""
Utilities module consisting of FIFOQueue
"""

from .nodes import QueueNode


class FIFOQueue:
    """
    Represents a First-In-First-Out (FIFO) Queue using a
    class-based linked list. Each QueueNode will contain a
    graph node and the path until that node.

    Attributes:
        front: Reference to the front (first) node in the queue.
        rear: Reference to the rear (last) node in the queue.
    """

    def __init__(self):
        """
        Initializes an empty FIFOQueue.
        """
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.front is None

    def is_exists(self, data):
        """
        Checks if a given element exists in the Queue.

        Args:
            data: The element to check for existence in the Queue.

        Returns:
            bool: True if the element exists in the Queue, False otherwise.
        """
        current = self.front
        while current is not None:
            if current.data == data:
                return True
            current = current.get_next()
        return False

    def enqueue(self, data, path):
        """
        Enqueues (adds) an element to the rear of the queue.

        Args:
            data: The data to be enqueued.
            path: The path associated with the data.
        """
        new_node = QueueNode(data, path)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

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
        data = self.front.get_data()
        path = self.front.get_path()
        self.front = self.front.get_next()
        if self.front is None:
            self.rear = None
        return data, path
