# Last updated: 12/26/2025, 3:54:03 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        freqs = {}
4        maxFreq = 0
5        currLen = 0
6
7        i = 0
8        j = 0
9
10        while j < len(s):
11            print('curr: ' + str(s[j]) + ', ' + str(j))
12
13            # update hash map
14            if s[j] in freqs.keys():
15                freqs[s[j]] += 1
16            else: 
17                freqs[s[j]] = 1
18
19            currLen = j - i + 1
20            maxFreq = max(freqs.values())
21
22            print('currLen: ' + str(currLen) + 
23                ', maxFreq: ' + str(maxFreq))
24
25            # check if can continue
26            if currLen - maxFreq > k: # can't continue, move up i
27                freqs[s[i]] -= 1
28                i += 1
29                
30            maxFreq = max(maxFreq, j - i + 1)
31            j += 1
32
33        return maxFreq