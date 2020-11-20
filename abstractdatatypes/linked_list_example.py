from abstractdatatypes.linked_list import Node
from abstractdatatypes.linked_list import LinkedList

n1 = Node('First')
print(n1)


ll = LinkedList()
print('ll.is_empty():', ll.is_empty())

ll.add(42)
ll.add(12)
ll.add(21)
ll.add(10)

print('ll.is_empty():', ll.is_empty())
print('ll.size():', ll.size())

print(ll)

print('ll.contains(21):', ll.contains(21))
print('ll.find(21):', ll.find(21))

ll.remove(12)
print(ll)

ll.insert(75, 21)
print(ll)

