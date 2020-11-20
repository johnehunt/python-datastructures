# Instrumented version of the unordered link list type

instrumentation_on = False


def set_instruction_on():
    global instrumentation_on
    instrumentation_on = True


class Node:
    """ Represents a node within a Linked List ADT"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return 'Node(' + str(self.data) + ')'


class LinkedList:
    """ Represents an unordered list in Python"""

    def __init__(self):
        if instrumentation_on: print('O(1)')
        self.head = None

    def is_empty(self):
        if instrumentation_on: print('O(1)')
        return self.head is None

    def add(self, item):
        _operation_count = 1
        temp = Node(item)
        temp.set_next(self.head)
        _operation_count += 1
        self.head = temp
        if instrumentation_on:
            print('O(' + str(_operation_count) + ')')

    def size(self):
        _operation_count = 1
        current = self.head

        count = 0
        while current is not None:
            _operation_count += 1
            count = count + 1
            current = current.get_next()

        if instrumentation_on: print('O(' + str(_operation_count) + ')')
        return count

    def contains(self, item):
        return self.find(item) is not None

    def find(self, item):
        _operation_count = 1
        current = self.head

        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                _operation_count += 1
                current = current.get_next()

        if instrumentation_on: print('O(' + str(_operation_count) + ')')

        return current

    def remove(self, item):
        _operation_count = 1;
        current = self.head

        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                _operation_count += 1
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        _operation_count += 1  # for above operation
        if instrumentation_on: print('O(' + str(_operation_count) + ')')

    def insert(self, data, after):
        node = self.find(after)
        if node is None:
            raise ValueError('unknown node value: ' + str(after))
        next_node = node.get_next()
        new_node = Node(data)
        node.set_next(new_node)
        new_node.set_next(next_node)

    # Implement Prepend and append
    # How can you make append as efficient as prepend?

    def __str__(self):
        current = self.head
        result = '[ '
        end_of_data = False
        while not end_of_data:
            if current is not None:
                result = result + str(current) + ' '
                current = current.get_next()
            else:
                end_of_data = True
        result = result + ']'
        return result

    # Support the length protocol
    def __len__(self):
        return self.size()
