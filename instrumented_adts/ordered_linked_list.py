# Instrumented version of the ordered link list type

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


class OrderedLinkedList:

    # Following methods are the same as for an unorder linked list

    def __init__(self):
        if instrumentation_on: print('O(1)')
        self.head = None

    def is_empty(self):
        if instrumentation_on: print('O(1)')
        return self.head is None

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

    def remove(self, item):
        _operation_count = 1
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

        _operation_count += 1 # for above operation
        if instrumentation_on: print('O(' + str(_operation_count) + ')')

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

    def __len__(self):
        return self.size()

    # Differences relative to an unordered linked list - and no insert

    def add(self, item):
        """ Add a value into the correct location within the list """

        _operation_count = 1

        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                _operation_count += 1
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

        _operation_count += 1  # for above operation
        if instrumentation_on:
            print('O(' + str(_operation_count) + ')')

    def find(self, item):
        """ Modified to exit when we have passed the point
        where the node should be located. This makes it
        more efficient. """

        _operation_count = 1

        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    _operation_count += 1
                    current = current.get_next()

        if instrumentation_on: print('O(' + str(_operation_count) + ')')

        return found
