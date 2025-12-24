# Last updated: 12/23/2025, 4:12:16 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        l1 = list1
9        l2 = list2
10
11        mll = None
12        mllend = None
13
14        while l1 or l2:
15            transplant = None
16
17            if l1 is None:
18                transplant = l2
19                l2 = l2.next
20                transplant.next = None
21            elif l2 is None:
22                transplant = l1
23                l1 = l1.next
24                transplant.next = None
25            else:
26                if l1.val < l2.val:
27                    transplant = l1
28                    l1 = l1.next
29                    transplant.next = None
30                else:
31                    transplant = l2
32                    l2 = l2.next
33                    transplant.next = None
34
35            if not mll:
36                mll = transplant
37                mllend = transplant
38            else:
39                mllend.next = transplant
40                mllend = mllend.next
41
42        return mll