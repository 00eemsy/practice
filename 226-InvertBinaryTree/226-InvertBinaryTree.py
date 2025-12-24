# Last updated: 12/23/2025, 4:14:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if root is not None:
10            l = root.left
11            r = root.right
12
13            root.right = self.invertTree(l)
14            root.left = self.invertTree(r)
15
16        return root 