# Last updated: 1/29/2026, 4:05:03 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        d = {}
4        m = (0,0)
5        i = len(s) - 1
6
7        while i >= 0:
8            for j in range(i, len(s)):
9                # print('i: ' + str(i) + '/' + s[i] + ', j: ' + str(j) + '/' +  s[j])
10                if i == j: # one letter
11                    d[(i,j)] = True
12                elif i+1 == j: # two letters
13                    if s[i] == s[j]:
14                        d[(i,j)] = True
15
16                        if m[1] - m[0] < j - i:
17                            m = (i,j)
18                    else:
19                        d[(i,j)] = False
20                else: # at least 1 letter w/in start & end
21                    # print('d[(i+1,j-1)]: ' + str(d[(i+1,j-1)]))
22                    if d[(i+1,j-1)] == True and s[i] == s[j]:
23                        d[(i,j)] = True
24
25                        if m[1] - m[0] < j - i:
26                            m = (i,j)
27                    else:
28                        d[(i,j)] = False
29
30                # print('m: ' + str(m))
31            i -= 1
32        
33        return s[m[0]:m[1]+1]
34        
35