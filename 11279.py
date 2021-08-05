# https://www.acmicpc.net/problem/11279

import heapq
import sys

input = sys.stdin.readline
N = int(input())

data = []
for i in range(N):
    x = int(input())
    if not x and data:
        print(-heapq.heappop(data))
    elif x:
        heapq.heappush(data, -x)
    else:
        print(0)
