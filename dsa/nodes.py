class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return self._in_order_traversal(self)

    def _in_order_traversal(self, node):
        if node is None:
            return ""
        left_str = self._in_order_traversal(node.left)
        right_str = self._in_order_traversal(node.right)
        return f"{left_str}{node.value} {right_str}"

# Example usage:

# Creating a simple binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Printing the binary tree nodes as a string
print("Binary tree nodes (in-order):", str(root))