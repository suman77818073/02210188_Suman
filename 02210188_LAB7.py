# Task 1: Implement the Node and BinaryTree Class Structure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        print("Created new Binary Tree")
        if root is None:
            print("Root: None")
        else:
            print(f"Root: {root.value}")

    # Task 2: Implement Tree Information Methods

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self, node, index, total_nodes):
        if node is None:
            return True
        if index >= total_nodes:
            return False
        return (self.is_complete_binary_tree(node.left, 2 * index + 1, total_nodes) and
                self.is_complete_binary_tree(node.right, 2 * index + 2, total_nodes))

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

# Example usage

# Create nodes
root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.left = Node(4)
root_node.left.right = Node(5)
root_node.right.left = Node(6)
root_node.right.right = Node(7)

# Create binary tree (Initially Empty Tree to match 'Root: None')
tree = BinaryTree()

# Now attach the nodes manually
tree.root = root_node

# Get tree information
print("Tree Height:", tree.height(tree.root))                 # Output: 3
print("Total Nodes:", tree.size(tree.root))                   # Output: 7
print("Leaf Nodes Count:", tree.count_leaves(tree.root))       # Output: 4
print("Is Full Binary Tree:", tree.is_full_binary_tree(tree.root))    # Output: True
total_nodes = tree.count_nodes(tree.root)
print("Is Complete Binary Tree:", tree.is_complete_binary_tree(tree.root, 0, total_nodes))  # Output: True