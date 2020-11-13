class BasicQueue:
    """ Queue ADT
    A queue is an ordered collection of items where
    the addition of new items happens at one end,
    called the “rear,” and the removal of existing
    items occurs at the other end, commonly called
    the “front.” As an element enters the queue it
    starts at the rear and makes its way toward the
    front, waiting until that time when it is the next
    element to be removed.
    """

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def enqueue(self, item):
        self.data.insert(0, item)

    def dequeue(self):
        return self.data.pop()

    def size(self):
        return len(self.data)

    def clear(self):
        self.data = []

    def __str__(self):
        return 'Queue' + str(self.data)

    # Implement the length protocol
    def __len__(self):
        return self.size()

    # Implement the iterable protocol
    def __iter__(self):
        temp = self.data.copy()
        temp.reverse()
        return iter(temp)
