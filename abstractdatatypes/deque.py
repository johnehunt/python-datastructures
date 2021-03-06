class Deque:

    """A Deque ADT in Python.
    Also known as a double-ended queue,
    is an ordered collection of items similar to the queue.
    It has two ends, a front and a rear, and the items
    remain positioned in the collection.
    """

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def add_front(self, item):
        self.data.append(item)

    def add_rear(self, item):
        self.data.insert(0,item)

    def remove_front(self):
        return self.data.pop()

    def remove_back(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

    def clear(self):
        self.data = []

    def __str__(self):
        return 'Deque' + str(self.data)

    # Implement the length protocol
    def __len__(self):
        return self.size()

    # Implement the iterable protocol
    def __iter__(self):
        temp = self.data.copy()
        temp.reverse()
        return iter(temp)
