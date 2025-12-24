# Last updated: 12/23/2025, 4:01:14 PM
1class DLLNode:
2    def __init__(self, val):
3        self.val = val
4        self.prev = None
5        self.next = None
6
7class Solution:
8    def longestConsecutive(self, nums: List[int]) -> int:
9        d = {}
10
11        for n in set(nums):
12            n_node = DLLNode(n)
13
14            d[n] = n_node
15
16            if n-1 in d.keys():
17                d[n].prev = d[n-1]
18                d[n-1].next = d[n]
19            if n+1 in d.keys():
20                d[n].next = d[n+1]
21                d[n+1].prev = d[n]
22
23        longest = 0
24
25        for n in d.keys():
26            if d[n].prev == None: # root! count!
27                count = 0
28                curr = d[n]
29
30                while curr:
31                    curr = curr.next
32                    count += 1
33
34                if count > longest:
35                    longest = count
36
37        return longest
38