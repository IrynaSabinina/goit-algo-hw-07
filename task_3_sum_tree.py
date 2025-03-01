# Node structure for BST or AVL Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to calculate the sum of all values in a BST or AVL tree
def sum_tree(root):
    if root is None:
        return 0  # Base case: empty tree has sum = 0
    
    return root.key + sum_tree(root.left) + sum_tree(root.right)

# Binary Search Tree (BST) implementation
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

# Example usage
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)
bst.insert(3)

# Find the sum of all values in BST
total_sum = sum_tree(bst.root)
print("Sum of all values in BST:", total_sum)  # Output: 53
