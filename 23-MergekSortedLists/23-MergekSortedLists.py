# Last updated: 12/30/2025, 11:29:41 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        head = None
9        curr = None
10
11        # audit lists, del blank lists
12        to_del = []
13
14        for i in range(len(lists)):
15            if lists[i] == None:
16                to_del.append(i)
17
18        n = len(to_del) - 1
19
20        while n >= 0:
21            lists.pop(to_del[n])
22            n -= 1
23
24        while len(lists) > 0:
25            # find min
26            min = 0
27
28            for i in range(len(lists)):
29                if lists[min].val > lists[i].val:
30                    min = i
31
32            # append
33            if head == None:
34                head = lists[min]
35                curr = head
36            else:
37                curr.next = lists[min]
38                curr = curr.next
39
40            if lists[min].next == None:
41                lists.pop(min)
42            else:
43                lists[min] = lists[min].next
44
45        return head