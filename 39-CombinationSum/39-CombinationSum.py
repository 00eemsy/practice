# Last updated: 1/4/2026, 3:41:18 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4
5        def helper(i, curr, sum):
6            # print('i: ' + str(i) + ', curr: ' + str(curr) + 'sum: ' + str(sum))
7            # print('res: ' + str(res))
8            if sum == target:
9                res.append(curr[::])
10                # print('hit the target! new res: ' + str(res))
11                return
12            elif sum > target:
13                print('overshot')
14                return
15            for j in range(i, len(candidates)):
16                curr.append(candidates[j])
17                helper(j, curr, sum + candidates[j])
18                curr.pop()
19                # helper(j, curr, sum)
20
21        helper(0, [], 0)
22        return res