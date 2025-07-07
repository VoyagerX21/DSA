#!/usr/bin/env python3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        def helper_recover(root):
            if root is None:
                return
            if root.left:
                root.left.val = 2*root.val+1
                helper_recover(root.left)
            if root.right:
                root.right.val = 2*root.val+2
                helper_recover(root.right)
        root.val = 0
        helper_recover(root)
        ln = dict()
        def order(root):
            if root is None:
                return
            ln[root.val] = 1
            if root.left:
                order(root.left)
            if root.right:
                order(root.right)
        
        order(root)
        self.ds = ln

    def find(self, target: int) -> bool:
        try:
            return bool(self.ds[target])
        except:
            return False

root = TreeNode(-1)
root.right = TreeNode(-1)
root.left = TreeNode(-1)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(-1)
obj = FindElements(root)
obj.find(3)