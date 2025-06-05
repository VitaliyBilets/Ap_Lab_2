class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(start_node: TreeNode) -> int:
    def dfs(node, depth):
        if not node:
            return 0

        left_depth = dfs(node.left, depth + 1)
        right_depth = dfs(node.right, depth + 1)
        return depth + left_depth + right_depth

    return dfs(start_node, 0)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print( sum_of_depths(start_node = root.left ))
