class Stack:
    """ A simple Stack ADT """

    def __init__(self):
        self.contents = []

    def is_empty(self):
        return self.contents == []

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        return self.contents.pop()

    def peek(self):
        return self.contents[len(self.contents) - 1]

    def size(self):
        return len(self.contents)

    def clear(self):
        self.contents = []
