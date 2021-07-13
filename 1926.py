# https://www.acmicpc.net/problem/1926
# 오랜만에 bfs문제 풀기. 평범한 bfs 문제였다.


from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(width):
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0 <= nx < n and 0 <= ny < m and painting[nx][ny] and not visited[nx][ny]:
                q.append([nx, ny])
                width += 1
                visited[nx][ny] = 1
    return width


n, m = map(int, input().split())

painting = []
for _ in range(n):
    painting.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

cnt = 0
res = 0
for i in range(n):
    for j in range(m):
        if painting[i][j] and not visited[i][j]:
            q = deque([[i, j]])
            visited[i][j] = 1
            cnt += 1
            temp = bfs(1)
            if temp > res:
                res = temp

print(cnt, res, sep='\n')