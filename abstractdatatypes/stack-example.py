# Example program using a stack

from abstractdatatypes.stack import Stack

stack = Stack()
print('stack.is_empty():', stack.is_empty())

stack.push("first")
stack.push("second")
stack.push("third")

print(stack)
print(len(stack))
for item in stack:
    print(item, end='')
print()

print('stack.peek():', stack.peek())

item = stack.pop()
print('1st popped item', item)

item = stack.pop()
print('2nd popped item', item)

item = stack.pop()
print('3rd popped item', item)

print(len(stack))
