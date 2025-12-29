# Last updated: 12/28/2025, 6:04:07 PM
1class Solution:
2    def search(self, nums, target: int) -> int:
3        i = self.findMin(nums)
4
5        if nums[i] == target:
6            return i
7
8        if nums[0] > target or i == 0:
9            arr = nums[i:]
10        else:
11            arr = nums[:i]
12
13        j = self.binarySearch(arr, target, 0, len(arr)-1)
14
15        if j == -1:
16            return j
17        elif nums[0] > target:
18            return i + j
19        else: return j
20
21    def findMin(self, nums):
22        curr = 0
23        prev = 0
24
25        if len(nums) == 1:
26            return 0
27
28        while True:
29            if nums[curr-1] > nums[curr]:
30                return curr
31            else:
32                if nums[prev] > nums[curr]:
33                    curr = prev + (curr - prev)//2
34                else:
35                    prev = curr
36                    curr += (len(nums) - curr)//2
37
38    def binarySearch(self, arr, target, low, high):
39        while low <= high:
40            mid = (low+high)//2
41            
42            if arr[mid] == target:
43                return mid
44            elif arr[mid] < target:
45                low = mid + 1
46            else:
47                high = mid - 1
48
49        return -1
50        