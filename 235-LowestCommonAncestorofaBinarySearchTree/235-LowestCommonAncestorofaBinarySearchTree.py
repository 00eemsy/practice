# Last updated: 1/5/2026, 3:46:46 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        def LCA(n):
11            # print('n: ' + str(n.val))
12            # check if val is descendant
13            currP = False
14            currQ = False
15
16            if n.val == p.val:
17                currP = True
18            elif n.val == q.val:
19                currQ = True
20            
21            l = None
22            r = None
23
24            pFlag = False
25            qFlag = False
26
27            if n.left:
28                l = LCA(n.left)
29            
30                if type(l) == list:
31                    if l[0] == True and l[1] == True:
32                        return n
33                    else:
34                        pFlag = l[0] or pFlag
35                        qFlag = l[1] or qFlag
36                elif l != None:
37                    return l
38            if n.right:
39                r = LCA(n.right)
40            
41                if type(r) == list:
42                    if r[0] == True and r[1] == True:
43                        return n
44                    else:
45                        pFlag = r[0] or pFlag
46                        qFlag = r[1] or qFlag
47                elif r != None:
48                    return r
49            
50            print('pFlag: ' + str(pFlag) + ', qFlag: ' + str(qFlag)
51                + ', currP: ' + str(currP) + ', currQ: ' + str(currQ))
52
53            if pFlag == True and qFlag == True:
54                return n
55            if (pFlag or qFlag) and (currP or currQ):
56                return n
57            else:
58                return([currP or pFlag, currQ or qFlag])
59
60        return LCA(root)