# Last updated: 12/23/2025, 3:56:38 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seenBefore = {}
4
5        for i in range(0,len(nums)):
6            n = nums[i]
7
8            if (target - n) in seenBefore.keys():
9                return [seenBefore[target-n], i]
10            else:
11                seenBefore[n] = i