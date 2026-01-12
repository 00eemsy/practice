# Last updated: 1/12/2026, 3:34:32 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        s = [[heights[0], 0]]
4        m = 0
5
6        for i in range(len(heights)):
7            last = s[-1]
8            popped = False
9
10            while len(s) > 0 and s[-1][0] > heights[i]:
11                popped = True
12                last = s.pop()
13                
14                m = max(m, last[0] * (i - last[1]))
15
16            index = last[1]
17
18            # width = i - last[1] + 1
19            # h = min(heights[i], last[0])
20
21            # m = max(m, h*width)
22
23            if popped:
24                s.append([heights[i], index])
25            else:
26                s.append([heights[i], i])
27
28        while len(s) > 0:
29            last = s.pop()
30            m = max(m, last[0] * (len(heights) - last[1]))
31
32        return m