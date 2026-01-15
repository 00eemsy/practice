# Last updated: 1/15/2026, 12:05:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        count = 0
10        ret = None
11
12        def helper(curr):
13            nonlocal count, k, ret
14
15            if count > k:
16                return 
17
18            l, r = None, None
19
20            if curr.left:
21                l = helper(curr.left)
22
23            count += 1
24
25            if count == k:
26                ret = curr.val
27                return
28
29            if curr.right:
30                r = helper(curr.right)
31
32        helper(root)
33        return ret