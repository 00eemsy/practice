# Last updated: 3/5/2026, 12:17:40 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        d = {len(cost)-1: cost[-1], len(cost)-2: cost[len(cost)-2]}
4
5        i = len(cost)-3
6
7        while i >= 0:
8            d[i] = cost[i] + min(d[i+1], d[i+2])
9            i -= 1
10
11        return min(d[0], d[1])