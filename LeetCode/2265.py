# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        global counter
        counter = 0
        def dfs(root):
            global counter
            sum = root.val
            n = 1
            if root.left:
                l = dfs(root.left)
                sum += l[0]
                n += l[1]
            if root.right:
                l = dfs(root.right)
                sum += l[0]
                n += l[1]
            if root.val == sum//n:
                counter += 1
            return sum, n

        dfs(root)
        return counter

root = TreeNode(4)
root.left = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
obj = Solution()
print(obj.averageOfSubtree(root))