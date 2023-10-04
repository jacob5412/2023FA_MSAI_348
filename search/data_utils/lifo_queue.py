"""
Utilities module consisting of LIFOQueue
"""

from .nodes import QueueNode


class LIFOQueue:
    """
    Represents a stack implemented using a class-based linked list. This is
    a Last-In-First-Out (LIFO) queue. Each QueueNode will contain a graph
    node and the path until that node.

    Attributes:
        top: A reference to the top element in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.top = None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top is None

    def push(self, data, path):
        """
        Pushes (adds) an element onto the top of the stack.

        Args:
            data: The data to be pushed onto the stack.
            path: The path associated with the data.
        """
        new_node = QueueNode(data, path)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Pops (removes and returns) the element from the top of the stack.

        Returns:
            data: The data popped from the top of the stack.

        Raises:
            IndexError: If the stack is empty when pop is called.
        """
        if not self.is_empty():
            data = self.top.get_data()
            path = self.top.get_path()
            self.top = self.top.get_next()
            return data, path
        raise IndexError("Stack is empty")

    def is_exists(self, data):
        """
        Checks if a given element exists in the Stack.

        Args:
            data: The element to check for existence in the Stack.

        Returns:
            bool: True if the element exists in the Stack, False otherwise.
        """
        current = self.top
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False
