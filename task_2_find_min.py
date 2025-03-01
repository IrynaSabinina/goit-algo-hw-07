# Node structure for BST or AVL Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to find the minimum value in a BST or AVL tree
def find_min(root):
    if root is None:
        return None  # Handle empty tree case
    
    current = root
    while current.left:  # Traverse to the leftmost node
        current = current.left
    
    return current.key  # Return the smallest value

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

# Find the smallest value in BST
min_value = find_min(bst.root)
print("Smallest value in BST:", min_value)  # Output: 3
