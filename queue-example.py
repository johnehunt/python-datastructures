from queue import BasicQueue

queue = BasicQueue()

print('queue.is_empty():', queue.is_empty())

queue.enqueue("First")
queue.enqueue("Second")
queue.enqueue("Third")
print(queue)

print('queue.size():', queue.size())

print('first dequeue:', queue.dequeue())
print('second dequeue:', queue.dequeue())
print('third dequeue:', queue.dequeue())

print(queue)