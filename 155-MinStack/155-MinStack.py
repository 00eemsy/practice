# Last updated: 12/23/2025, 4:07:45 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minstack = []
6
7    def push(self, val: int) -> None:
8        i = 0
9
10        while i < len(self.minstack) and self.minstack[i] < val:
11            i+= 1
12
13        self.minstack.insert(i, val)
14        self.stack.insert(0, val)
15        # print('stack: ' + str(self.stack))
16        # print('minstack: ' + str(self.minstack))
17
18    def pop(self) -> None:
19        to_pop = self.stack[0]
20        self.stack = self.stack[1:]
21        
22        self.minstack.remove(to_pop)
23
24        # print('stack: ' + str(self.stack))
25        # print('minstack: ' + str(self.minstack))
26        
27
28    def top(self) -> int:
29        return self.stack[0]
30        
31
32    def getMin(self) -> int:
33        return self.minstack[0]
34        
35
36
37# Your MinStack object will be instantiated and called as such:
38# obj = MinStack()
39# obj.push(val)
40# obj.pop()
41# param_3 = obj.top()
42# param_4 = obj.getMin()