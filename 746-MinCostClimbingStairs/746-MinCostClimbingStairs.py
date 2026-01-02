# Last updated: 1/2/2026, 3:38:45 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        d = {0:cost[0], 1:cost[1]}
4
5        for i in range(2,len(cost)):
6            d[i] = min(d[i-1], d[i-2]) + cost[i]
7
8        return min(d[len(cost) - 1], d[len(cost) - 2])