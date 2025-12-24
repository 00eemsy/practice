# Last updated: 12/23/2025, 4:13:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head):
8        if head == None:
9            return None
10        elif head.next == None:
11            return head
12        else:
13            curr = head.next
14            prev = head
15            future = curr.next
16            flag = False
17
18            while future != None or flag == False:
19                if future == None:
20                    flag = True
21                
22                curr.next = prev
23                
24                if prev == head:
25                    prev.next = None
26
27                prev = curr
28                curr = future
29                if future:
30                    future = future.next
31
32        return prev
33
34    def reorderList(self, head: Optional[ListNode]) -> None:
35        # find len of list
36        length = 0
37        curr = head
38
39        while curr.next != None:
40            length += 1
41            curr = curr.next
42
43        split_length = length//2
44
45        # split
46        curr = head
47
48        while split_length > 0:
49            curr = curr.next
50            split_length -= 1
51
52        h2 = curr.next
53        curr.next = None
54
55        # reverse
56        h2 = self.reverseList(h2)
57
58        # combine
59        c1 = head
60
61        while h2 != None:
62            f1 = c1.next
63            f2 = h2.next
64
65            c1.next = h2
66            h2.next = f1
67
68            h2 = f2
69            if f2:
70                f2 = f2.next
71            c1 = f1
72            if f1:
73                f1 = f1.next
74
75        