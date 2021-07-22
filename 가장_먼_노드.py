# https://programmers.co.kr/learn/courses/30/lessons/49189
# bfs 방식으로 풀었다.


from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    q = deque([[1, 0]])
    visited = [0] * (n+1)
    visited[1] = 1
    
    while q:
        x, cnt = q.popleft()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = cnt+1
                q.append([y, cnt+1])

    for v in visited:
        if v == cnt:
            answer += 1
    return answer