# Last updated: 1/24/2026, 12:55:26 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        # from 0->len(nums)-2
4        rob1 = 0
5        d = {0: nums[0]}
6
7        for i in range(1, len(nums)-1):
8            if i == 1:
9                d[1] = nums[1]
10            elif i == 2:
11                d[2] = nums[2] + d[0]
12            else:
13                d[i] = nums[i] + max(d[i-2], d[i-3])
14        
15        if len(nums) == 1:
16            rob1 = nums[0]
17        elif len(nums) == 2:
18            rob1 = d[len(nums)-2]
19        else:
20            rob1 = max(d[len(nums)-2], d[len(nums)-3])
21
22        # now from 1->len(nums)-1
23        rob2 = 0
24        d = {0: 0}
25
26        for i in range(1, len(nums)):
27            if i == 1:
28                d[1] = nums[1]
29            elif i == 2:
30                d[2] = nums[2] + d[0]
31            else:
32                d[i] = nums[i] + max(d[i-2], d[i-3])
33        
34        if len(nums) > 1:
35            rob2 = max(d[len(nums)-1], d[len(nums)-2])
36
37        return max(rob1, rob2)