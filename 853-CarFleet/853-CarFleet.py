# Last updated: 12/23/2025, 4:08:52 PM
1class Node:
2    def __init__(self, curr, speed):
3        self.curr = curr
4        self.speed = speed
5
6class Solution:
7    def weirdMergeSort(self, arr):
8        if len(arr) <= 1:
9            return arr
10        else:
11            mid = len(arr)//2
12
13            left = self.weirdMergeSort(arr[0:mid])
14            right = self.weirdMergeSort(arr[mid:])
15
16            return self.weirdMerge(left, right)
17
18    def weirdMerge(self, l, r):
19        l_count = 0
20        r_count = 0
21
22        merged = []
23
24        while l_count < len(l) or r_count < len(r):
25            if l_count >= len(l):
26                merged.append(r[r_count])
27                r_count += 1
28            elif r_count >= len(r):
29                merged.append(l[l_count])
30                l_count += 1
31            elif l[l_count] > r[r_count]:
32                merged.append(l[l_count])
33                l_count += 1
34            else:
35                merged.append(r[r_count])
36                r_count += 1
37
38        return merged
39
40
41    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
42        # make dict storing speeds and positions
43        speeds_dict = {}
44
45        for i in range(0, len(position)):
46            speeds_dict[position[i]] = speed[i]
47        
48        # sort positions from high to low
49        sorted_p = self.weirdMergeSort(position)
50
51        # iter through each step
52        fleets = 0
53        max_time = 0
54
55        for p in sorted_p:
56            spd = speeds_dict[p]
57            time = (target - p) / spd # apparently you need to do it by arrival time not in int steps
58
59            if time > max_time:
60                fleets += 1
61                max_time = time
62
63        return fleets