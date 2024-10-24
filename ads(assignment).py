class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if current.left is None:
            current.left = new_node
        elif current.right is None:
            current.right = new_node
        else:
            self._insert(current.left, new_node)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

bt = BinaryTree()
bt.root = Node(30)
bt.root.left = Node(11)
bt.root.right = Node(20)
bt.root.left.left = Node(18)
bt.root.left.right = Node(19)
bt.root.left.left.left = Node(17)
bt.root.right.right = Node(21)


print("Inorder Traversal:")
bt.inorder(bt.root) 
print()
print("Preorder Traversal:")
bt.preorder(bt.root)  
print()
print("Postorder Traversal:")
bt.postorder(bt.root)  
print()
