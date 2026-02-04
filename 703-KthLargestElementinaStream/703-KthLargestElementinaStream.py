# Last updated: 2/4/2026, 10:47:04 AM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.k = k
5        self.heap = nums
6
7        for i in range(len(nums) // 2 - 1, -1, -1):
8            self.heapify(i) #heapq.heapify(self.heap)
9        
10        while len(self.heap) > k:
11            self.heap[0] = self.heap[-1]
12            self.heap.pop()
13            self.heapify(0)
14
15        # print('heap: ' + str(self.heap))
16
17    def add(self, val: int) -> int:
18        # print('val: ' + str(val))
19        self.heap.append(val)
20        i = len(self.heap) - 1
21
22        while i > 0 and self.heap[(i-1)//2] > self.heap[i]:
23            # print('i: ' + str(i) + ' or ' + str(self.heap[i]), 'i//2: ' + str(i//2) + ' or ' + str(self.heap[i//2]))
24            temp = [self.heap[(i-1)//2], self.heap[i]]
25
26            self.heap[(i-1)//2] = temp[1]
27            self.heap[i] = temp[0]
28
29            i = (i-1)//2
30
31        if len(self.heap) > self.k:
32            # print('heapify!')
33            self.heap[0] = self.heap[-1]
34            self.heap.pop()
35            self.heapify(0)
36
37        # print('heap: ' + str(self.heap))
38
39        if len(self.heap) == self.k:
40            return self.heap[0]
41        else:
42            return
43
44    def heapify(self, i):
45        l = 2*i + 1
46        r = 2*i + 2
47
48        smallest = i
49
50        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
51            smallest = l
52        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
53            smallest = r
54
55        if smallest != i:
56            temp = [self.heap[smallest], self.heap[i]]
57            
58            self.heap[i] = temp[0]
59            self.heap[smallest] = temp[1]
60
61            self.heapify(smallest)
62            
63
64
65# Your KthLargest object will be instantiated and called as such:
66# obj = KthLargest(k, nums)
67# param_1 = obj.add(val)