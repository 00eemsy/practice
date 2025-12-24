# Last updated: 12/23/2025, 4:01:50 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = s.lower()
4        arr = []
5
6        for char in s:
7            if char.isalnum():
8                arr.append(char) 
9
10        print(arr)
11
12        start = 0
13        end = len(arr) - 1
14
15        while start < end:
16            if arr[start] != arr[end]:
17                return False
18
19            start += 1
20            end -= 1
21
22        return True