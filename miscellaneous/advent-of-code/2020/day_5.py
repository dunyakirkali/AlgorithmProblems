from collections import defaultdict, deque, Counter
# d = deque()
# d.append(5)
# x = d.popleft()
import re
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist") 
# # or re.search
# >>> m.group(0)       # The entire match
# 'Isaac Newton'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'Isaac'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'Newton'
# >>> m.group(1, 2)    # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')
from heapq import heappush, heappop
# >>> heap = []
# >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# >>> for item in data:
# ...     heappush(heap, item)
# heap[0] is the smallest item
import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

if True:
    ans = list()

    while True:
        try:
            a = input()
            fb = a[:7]
            r = a[7:]
            x = 0
            n = 64
            # trans = {'F':}
            for l in fb:
                if l == 'B':
                    x += n
                n//=2
            # print(x)
            rr = 0
            n = 4
            print(r)
            for rrr in r:
                if rrr == 'R':
                    rr += n
                n//=2
            print(rr)
            sid = x*8 + rr
            print(sid)
            ans.append(sid)
        except EOFError:
            break
    
    print(max(ans))
    for i in range(max(ans)):
        if i not in ans:
            print(i)
else:
    pass