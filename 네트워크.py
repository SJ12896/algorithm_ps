# https://programmers.co.kr/learn/courses/30/lessons/43162
# dfs는 여러번 풀어봤지만 프로그래머스 방식으로 푸니까 약간 색다른 느낌이었다.

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        for j in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = 1
                dfs(stack, computers, visited)
                answer += 1
    
    return answer


def dfs(stack, computers, visited):
    while stack:
        x = stack.pop()
        for i in range(len(computers)):
            if i != x and not visited[i] and computers[x][i]:
                stack.append(i)
                visited[i] = 1