# Last updated: 1/11/2026, 5:51:03 PM
1class TrieNode:
2    def __init__(self, val):
3        self.val = val
4        self.next = {}
5
6class Trie:
7
8    def __init__(self):
9        self.root = TrieNode(None)
10        self.end = TrieNode('end')
11
12    def insert(self, word: str) -> None:
13        curr = self.root
14        seenBefore = True
15
16        for char in word:
17            if char in curr.next and seenBefore:
18                curr = curr.next[char]
19            else:
20                new = TrieNode(char)
21                curr.next[char] = new
22                curr = new
23
24        curr.next['end'] = self.end
25
26    def search(self, word: str) -> bool:
27        curr = self.root
28
29        for char in word:
30            if char in curr.next:
31                curr = curr.next[char]
32            else:
33                return False
34
35        if 'end' in curr.next:
36            return True
37        
38        return False
39
40    def startsWith(self, prefix: str) -> bool:
41        curr = self.root
42
43        for char in prefix:
44            if char in curr.next:
45                curr = curr.next[char]
46            else:
47                return False
48
49        return True
50
51
52# Your Trie object will be instantiated and called as such:
53# obj = Trie()
54# obj.insert(word)
55# param_2 = obj.search(word)
56# param_3 = obj.startsWith(prefix)