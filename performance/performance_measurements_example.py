from performance.ordered_linked_list import OrderedLinkedList
from performance.linked_list import LinkedList

import time

LOOP_SIZE = 1000

ll = LinkedList()
oll = OrderedLinkedList()

# Unordered Linked List timings
# ---------------------------
# Obtain system time before operations
print('Processing Unordered linked list')
start = time.time()

# Determine the time taken to add LOOP_SIZE numbers
for i in range(0, LOOP_SIZE):
    ll.add(i)

end = time.time()
print('UnorderedLinkedList time for ' + str(LOOP_SIZE) + ' additions:', end-start)
print()

# Ordered Linked List timings
# ---------------------------
# Obtain system time before operations
print('Processing Ordered linked list')
start = time.time()

# Determine the time taken to add LOOP_SIZE numbers
for i in range(0, LOOP_SIZE):
    oll.add(i)

end = time.time()
print('OrderedLinkedList time for '+ str(LOOP_SIZE) + ' additions:', end-start)
