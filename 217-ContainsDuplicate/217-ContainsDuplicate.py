# Last updated: 12/23/2025, 3:55:36 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        setNums = set(nums)
4
5        if len(setNums) == len(nums):
6            return False
7        else:
8            return True