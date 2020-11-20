from instrumented_adts.linked_list import LinkedList
from instrumented_adts.linked_list import set_instruction_on

LOOP_SIZE = 10

ll = LinkedList()

for i in range(0, LOOP_SIZE):
    ll.add(i)

set_instruction_on()

print('is_emtpy')
ll.is_empty()

print('add')
ll.add(11)

print('find(1)')
ll.find(1)

print('find(11)')
ll.find(11)
