# Last updated: 12/23/2025, 4:00:36 PM
1class Solution:
2    def checkRow(self, s, squareVal):
3        if len(s) > 0:
4            length = len(s)
5            s.add(squareVal)
6
7            if len(s) == length:
8                print('breaking bc: row')
9                return False
10        
11        else:
12            s.add(squareVal)
13
14        return True
15
16    def checkDict(self, index, d, squareVal, cb):
17        if index in d.keys():
18            length = len(d[index])
19            d[index].add(squareVal)
20
21            if len(d[index]) == length:
22                print('breaking bc: ' + cb)
23                return False
24
25        else:
26            d[index] = set(squareVal)
27
28        return True
29
30    def isValidSudoku(self, board: List[List[str]]) -> bool:
31        colDict = {} # {set(), set()...} per col
32        boxDict = {} # {set(), set()} per box
33
34        rowCount = 1
35
36        for i in range(9):
37            rowSet = set()
38
39            colCount = 0
40            # print('i = ' + str(i))
41            for j in range(9): # per row
42                # print('j = ' + str(j))
43                print('board[i][j] = ' + str(board[i][j]))
44
45                if board[i][j] != '.':
46                    # row logic
47                    if not self.checkRow(rowSet, board[i][j]):
48                        return False
49
50                    # column logic
51                    if not self.checkDict(j, colDict, board[i][j], 'col'):
52                        return False
53
54                    # box logic
55                    temp = rowCount + colCount
56                    print('boxIndex: ' + str(temp))
57
58                    if not self.checkDict(temp, boxDict, board[i][j], 'box'):
59                        return False
60
61                if j>0 and j%3 == 2:
62                    colCount += 1
63
64            if i>0 and i%3 == 2:
65                rowCount += 3
66
67        return True
68
69        