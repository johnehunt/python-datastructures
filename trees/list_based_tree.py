# Sample tree constructed using lists
test_tree = ['a',  # root
             ['b',  # left subtree
              ['d', [], []],
              ['e', [], []]],
             ['c',  # right subtree
              ['f', [], []],
              []]
             ]

print('tree', test_tree)
print('left subtree = ', test_tree[1])
print('root = ', test_tree[0])
print('right subtree = ', test_tree[2])


# Functions to make it easier to work with trees

def create_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_value(root):
    return root[0]


def set_root_value(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


# Program to exercise functions defined above

list_tree = create_tree(3)
insert_left(list_tree, 4)
insert_left(list_tree, 5)
insert_right(list_tree, 6)
insert_right(list_tree, 7)

print(list_tree)

l = get_left_child(list_tree)
print(l)

set_root_value(l, 9)
print(list_tree)
insert_left(l, 11)
print(list_tree)
print(get_right_child(get_right_child(list_tree)))
