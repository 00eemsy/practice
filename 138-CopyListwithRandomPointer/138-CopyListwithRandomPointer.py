# Last updated: 12/23/2025, 6:59:32 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        nodeBank = {}
13
14        # get vals
15        curr = head
16
17        while curr != None:
18            nodeBank[(curr.val, curr.next)] = Node(curr.val)
19            curr = curr.next
20
21        # connections (next, random)
22        curr = head
23
24        while curr != None:
25            n = nodeBank[(curr.val, curr.next)]
26
27            if curr.next != None:
28                n.next = nodeBank[(curr.next.val, curr.next.next)]
29            else:
30                n.next = None
31            
32            if curr.random != None:
33                n.random = nodeBank[(curr.random.val, curr.random.next)]
34            else:
35                n.random = None
36
37            curr = curr.next
38
39        new_head = None
40        
41        if head != None:
42            new_head = nodeBank[head.val, head.next]
43
44        return new_head