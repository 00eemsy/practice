# Last updated: 12/27/2025, 8:45:55 PM
1from collections import OrderedDict
2
3class LRUCache:
4    def __init__(self, capacity: int):
5        self.capacity = capacity
6        self.hash = OrderedDict()
7
8    def get(self, key: int) -> int:
9        # print('in GET:\nkey: ' + str(key))
10        if key in self.hash.keys():
11            val = self.hash.pop(key)
12            self.hash[key] = val
13            return self.hash[key]
14        else:
15            return -1
16
17    def put(self, key: int, value: int) -> None:
18        # print('in PUT:\nkey/value: ' + str(key) + '/' + str(value))
19        
20        try: 
21            self.hash.pop(key)
22        except:
23            pass
24        self.hash[key] = value
25
26        if len(self.hash) > self.capacity:
27            self.hash.popitem(last=False)
28
29        # print(self.hash)
30            
31
32
33# Your LRUCache object will be instantiated and called as such:
34# obj = LRUCache(capacity)
35# param_1 = obj.get(key)
36# obj.put(key,value)