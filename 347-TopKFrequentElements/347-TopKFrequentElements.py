# Last updated: 12/23/2025, 3:57:24 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        countDict = {}
4        freq = [[] for i in range(len(nums) + 1)]
5
6        for n in nums:
7            if n in countDict.keys():
8                countDict[n] += 1
9            else:
10                countDict[n] = 1
11
12        for n, val in countDict.items():
13            freq[val].append(n)
14
15        topK = []
16        currFreq = len(freq) - 1
17        
18        for i in range(0,k):
19            while len(freq[currFreq]) == 0:
20                currFreq -= 1
21
22            topK.append(freq[currFreq][-1])
23            freq[currFreq].remove(freq[currFreq][-1])
24
25        return topK