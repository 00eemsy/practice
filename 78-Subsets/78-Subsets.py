# Last updated: 1/4/2026, 2:50:25 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        return self.powerSet(nums, [])
4        
5    def powerSet(self, arr, s):
6        if arr not in s:
7            s.append(arr)
8
9        for i in range(len(arr)):
10            new_arr = []
11
12            if i == 0:
13                new_arr = arr[i+1:]
14            elif i == len(arr) - 1:
15                new_arr = arr[:i]
16            else:
17                new_arr = arr[:i] + arr[i+1:]
18
19            self.powerSet(new_arr, s)
20
21        return s