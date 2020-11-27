class BinaryTreeNode:
    def __init__(self, root_value):
        self.key = root_value
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTreeNode(new_node)
        else:
            t = BinaryTreeNode(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTreeNode(new_node)
        else:
            t = BinaryTreeNode(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key

    def __str__(self):
        return 'BinaryTreeNode(' + str(self.key) + \
               ', left child empty: ' + str(self.left_child is None) + \
               ', right child empty: ' + str(self.right_child is None) + \
               ')'


# Simple program illustrating use of BinaryTreeNode class

tree = BinaryTreeNode('a')
print(tree.get_root_value())
print(tree)
print(tree.get_left_child())

tree.insert_left('b')
print(tree.get_left_child())
print(tree.get_left_child().get_root_value())

tree.insert_right('c')
print(tree.get_right_child())
print(tree.get_right_child().get_root_value())

tree.get_right_child().set_root_value('hello')
print(tree.get_right_child().get_root_value())

print(tree)
