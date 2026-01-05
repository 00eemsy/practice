# Last updated: 1/4/2026, 5:44:58 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4
5        c = {}
6        c_init = {}
7
8        for n in range(len(candidates)):
9            if candidates[n] in c.keys():
10                c[candidates[n]] += 1
11            else:
12                c[candidates[n]] = 1
13                c_init[candidates[n]] = 0
14
15        keys = list(c.keys())
16
17        def helper(i, counts, sum):
18            # print("counts: " + str(counts) + ", sum: " + str(sum))
19            if sum == target:
20                curr = []
21                for key in counts.keys():
22                    for n in range(counts[key]):
23                        curr.append(key)
24
25                res.append(curr)
26                return
27            elif sum > target:
28                return
29            for j in range(i, len(keys)):
30                if counts[keys[j]] + 1 <= c[keys[j]]:
31                    counts[keys[j]] += 1
32                    helper(j, counts, sum + keys[j])
33                    counts[keys[j]] -= 1
34
35        helper(0, c_init, 0)
36        return res
37