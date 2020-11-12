from deque import Deque

d= Deque()
print(d.is_empty())

d.add_rear("first")
d.add_rear('second')
d.add_front('third')
d.add_front('fourth')

print(d)

print(d.size())

print(d.is_empty())

d.add_rear('fifth')

print(d.remove_rear())
print(d.remove_front())
