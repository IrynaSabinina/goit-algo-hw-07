# Node structure for BST or AVL Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to find the maximum value in a BST or AVL tree
def find_max(root):
    if root is None:
        return None  # Handle empty tree case
    
    current = root
    while current.right:  # Traverse to the rightmost node
        current = current.right
    
    return current.key  # Return the largest value

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
bst.insert(30)

# Find the largest value in BST
max_value = find_max(bst.root)
print("Largest value in BST:", max_value)  # Output: 30
