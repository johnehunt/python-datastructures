from performance.ordered_linked_list import OrderedLinkedList
from performance.linked_list import LinkedList

import time

# Try with
LOOP_SIZE = 10000
# LOOP_SIZE = 10000

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
print('UnorderedLinkedList time for add ' + str(LOOP_SIZE) + ':', end - start)

for i in range(0, LOOP_SIZE):
    ll.find(500)

end = time.time()
print('UnorderedLinkedList time for find ' + str(LOOP_SIZE) + ':', end - start)

print('-' * 30)

# Ordered Linked List timings
# ---------------------------
# Obtain system time before operations
print('Processing Ordered linked list')
start = time.time()

# Determine the time taken to add LOOP_SIZE numbers
for i in range(0, LOOP_SIZE):
    oll.add(i)

end = time.time()
print('OrderedLinkedList time for add ' + str(LOOP_SIZE) + ':', end - start)

start = time.time()

# Determine the time taken to add LOOP_SIZE numbers
for i in range(0, LOOP_SIZE):
    oll.find(500)

end = time.time()
print('OrderedLinkedList time for find ' + str(LOOP_SIZE) + ':', end - start)

# Sample output
# Processing Unordered linked list
# UnorderedLinkedList time for add 10000: 0.011484146118164062
# UnorderedLinkedList time for find 10000: 29.50747799873352
# ------------------------------
# Processing Ordered linked list
# OrderedLinkedList time for add 10000: 15.624212980270386
# OrderedLinkedList time for find 10000: 2.3151328563690186
