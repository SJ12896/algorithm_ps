# https://www.acmicpc.net/problem/11660
# 오랜만에 다이나믹 프로그래밍을 풀어서 잘 안풀렸다. 이런 경우에 처음부터 계산해주기
# 쉽도록 맨 윗 행과 맨 앞 열에 0을 추가해줘서 푸는 거 잊지 말기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[0] * (N+1)] 
for _ in range(N):
    temp = [0] + list(map(int, input().split()))
    table.append(temp)

for i in range(1, N+1):
    for j in range(1, N+1):
        table[i][j] = table[i][j] + table[i-1][j] + table[i][j-1] - table[i-1][j-1]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1]
    print(result)
