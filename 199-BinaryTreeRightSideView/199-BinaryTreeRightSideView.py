# Last updated: 1/6/2026, 2:26:25 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        q = []
10        ret = []
11        currLvl = []
12        count = 0
13
14        if root:
15            q.append([root, 0])
16        
17        while len(q) > 0:
18            n = q.pop(0)
19
20            # print('n: ' + str(n[0].val) + ', ' + str(n[1]))
21
22            if n[1] > count:
23                ret.append(currLvl.pop())
24                count = n[1]
25                currLvl = []
26            
27            currLvl.append(n[0].val)
28
29            if n[0].left:
30                q.append([n[0].left, n[1] + 1])
31            if n[0].right:
32                q.append([n[0].right, n[1] + 1])
33
34        if len(currLvl) > 0:
35            ret.append(currLvl.pop())
36
37        return ret
38