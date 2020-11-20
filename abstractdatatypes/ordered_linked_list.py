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
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head

        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def remove(self, item):
        current = self.head

        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

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
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def find(self, item):
        """ Modified to exit when we have passed the point
        where the node should be located. This makes it
        more efficient. """
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
                    current = current.get_next()

        return found
