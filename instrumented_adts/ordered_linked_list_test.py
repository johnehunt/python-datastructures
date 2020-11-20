from instrumented_adts.ordered_linked_list import OrderedLinkedList
from instrumented_adts.ordered_linked_list import set_instruction_on

LOOP_SIZE = 10

oll = OrderedLinkedList()

for i in range(0, LOOP_SIZE):
    oll.add(i)

set_instruction_on()

print('is_emtpy')
oll.is_empty()

print('add')
oll.add(11)

print('find(1)')
oll.find(1)

print('find(5)')
oll.find(5)

print('find(11)')
oll.find(11)
