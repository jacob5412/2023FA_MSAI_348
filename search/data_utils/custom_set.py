"""
Utilities module consisting of a Custom Set or Set
"""


class Set:
    """
    A simple Set class that allows adding and checking the
    existence of elements.

    Attributes:
        data_set (set): The underlying set that stores unique elements.
    """

    def __init__(self):
        """
        Initializes a new Set instance.
        """
        self.data_set = set()

    def is_exists(self, data):
        """
        Checks if a given element exists in the set.

        Args:
            data: The element to check for existence in the set.

        Returns:
            bool: True if the element exists in the set, False otherwise.
        """
        return data in self.data_set

    def enqueue(self, data):
        """
        Adds an element to the set if it does not already exist.

        Args:
            data: The element to add to the set.

        Returns:
            bool: True if the element is added to the set,
                  False if it already exists.
        """
        if not self.is_exists(data):
            self.data_set.add(data)
            return True
        return False

    def fetch_set(self):
        """
        Retrieves the current set.

        Returns:
            data_set: The set containing unique elements.
        """
        return self.data_set
