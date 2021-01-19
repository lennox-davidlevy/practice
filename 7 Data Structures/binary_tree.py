class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_child(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinaryTree(value)
            else:
                self.left.insert_child(value)
        elif value > self.value:
            if self.right == None:
                self.right = BinaryTree(value)
            else:
                self.right.insert_child(value)
        else:
            return "Value already exists!"

    def count_leaves(node):
        if node == None:
            return 0
        if node.left is None and node.right is None:
            return 1
        else:
            return count_leaves(node.left) + count_leaves(node.right)


new_tree = BinaryTree(10)
new_tree.insert_child(1)
new_tree.insert_child(1)
new_tree.insert_child(12)
new_tree.insert_child(3)
new_tree.insert_child(124)
print(new_tree.count_leaves(new_tree))
