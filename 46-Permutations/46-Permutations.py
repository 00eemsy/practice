# Last updated: 1/6/2026, 3:36:23 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        ret = []
4        length = len(nums)
5
6        def helper(curr, n):
7            # print('curr: ' + str(curr) + ', n: ' + str(n))
8            if len(curr) == length:
9                ret.append(curr[::])
10                return
11
12            for j in range(len(n)):
13                curr.append(nums[j])
14                temp = n.pop(j)
15                helper(curr, n)
16                curr.pop()
17                n.insert(j, temp)
18
19        helper([], nums)
20        return ret