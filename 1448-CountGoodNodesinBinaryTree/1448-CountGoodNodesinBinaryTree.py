# Last updated: 1/11/2026, 2:24:48 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        next = []
10        count = 0
11
12        if root:
13            next.append([root, root.val])
14
15        while len(next) > 0:
16            curr = next.pop(0)
17
18            if curr[0].val >= curr[1]:
19                count += 1
20
21            if curr[0].right:
22                next.insert(0,[curr[0].right, max(curr[1], curr[0].val)])
23            if curr[0].left:
24                next.insert(0, [curr[0].left, max(curr[1], curr[0].val)])
25
26        return count