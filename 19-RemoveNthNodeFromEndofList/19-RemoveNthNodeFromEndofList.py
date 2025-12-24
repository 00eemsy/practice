# Last updated: 12/23/2025, 4:13:50 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        og = head
9        count = 0
10
11        while og != None:
12            # traverse and get length of LL
13            count += 1
14            og = og.next
15
16        rm_count = count - n
17        curr = head
18        prev = None
19
20        while rm_count > 0:
21            # navigate to node to be rm-ed
22            prev = curr
23            curr = curr.next
24            rm_count -= 1
25
26        # removal
27
28        if prev: # if not [x] only
29            prev.next = curr.next
30        else:
31            head = curr.next
32        
33        curr.next = None
34
35        return head