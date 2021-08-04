# https://www.acmicpc.net/problem/1929

import math

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i)+1)):
        if not i % j:
            break
    else:
        print(i)