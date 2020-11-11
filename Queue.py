class Queue:
    """ Queue ADT """

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
