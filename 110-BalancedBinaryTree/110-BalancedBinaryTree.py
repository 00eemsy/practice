# Last updated: 12/26/2025, 2:01:43 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        if root == None:
10            return True
11        else:
12            result = self.traverse(root)
13
14            if result == False:
15                return False
16            else:
17                return True
18        
19    def traverse(self, n):   
20        if n.left == None and n.right == None:
21            return 1
22        else:
23            l = 0 
24            r = 0
25
26            if n.left:
27                l = self.traverse(n.left)
28            if n.right:
29                r = self.traverse(n.right)
30
31            print('n: ' + str(n.val) + 'l: ' + str(l) + '\nr: ' + str(r))
32
33            # check what to return
34            if type(l) == bool or type(r) == bool:
35                return False
36            else:
37                if abs(l-r) > 1:
38                    return False
39                else:
40                    return max(l,r) + 1