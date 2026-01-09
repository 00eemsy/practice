# Last updated: 1/9/2026, 3:34:18 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        ret = []
4        d = {}
5        keys = []
6
7        for n in nums:
8            if n in d:
9                d[n] += 1
10            else:
11                d[n] = 1
12                keys.append(n)
13
14        def helper(i, curr, d):
15            ret.append(curr[::])
16
17            n = i
18
19            while n < len(keys):
20                if d[keys[n]] > 0:
21                    d[keys[n]] -= 1
22                    curr.append(keys[n])
23                    helper(n, curr, d)
24                    d[keys[n]] += 1
25                    curr.pop()
26                
27                n += 1
28
29        helper(0, [], d)
30        return ret