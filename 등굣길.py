# https://programmers.co.kr/learn/courses/30/lessons/42898
# 첫번째 코드가 대체 왜 틀렸을까 계속 고민했다. 첫 행, 첫 열이 1이 아니고 더 많은 숫자가 나올 수 없을텐데 왜 틀렸는지 궁금했다.
# 알고보니 반대로 생각해야했다. 더 많은 숫자가 아니라 1이 아닌 0이 나와야 하는 상황을 막아버리는 풀이 방법이었다. 

# 틀린 방법
# def solution(m, n, puddles):
#     answer = 0
#     ways = [[0] * m for _ in range(n)]
#     for i, j in puddles:
#         ways[j-1][i-1] = -1
            
#     for i in range(n):
#         for j in range(m):
#             if ways[i][j] == -1:
#                 continue
#             if not i or not j:
#                 ways[i][j] = 1
#             else:
#                 a = 0 if ways[i-1][j] == -1 else ways[i-1][j]
#                 b = 0 if ways[i][j-1] == -1 else ways[i][j-1]
#                 ways[i][j] = (a+b) % 1000000007
#     print(ways)   
#     answer = ways[n-1][m-1]  
#     return answer

# 맞은 방법
# def solution(m, n, puddles):
#     answer = 0
#     ways = [[0] * m for _ in range(n)]
    
#     ways[0][0] = 1
#     for i, j in puddles:
#         ways[j-1][i-1] = -1
            
#     for i in range(n):
#         for j in range(m):
#             if ways[i][j] == -1 or (not i and not j):
#                 continue
                
#             a = 0 if ways[i-1][j] == -1 else ways[i-1][j]
#             b = 0 if ways[i][j-1] == -1 else ways[i][j-1]
#             ways[i][j] = (a+b) % 1000000007
 
#     answer = ways[n-1][m-1]  
#     return answer


def solution(m, n, puddles):
    answer = 0
    ways = [[0] * m for _ in range(n)]
    ways[0][0] = 1
            
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles or (not i and not j):
                continue
            ways[i][j] = (ways[i-1][j]+ways[i][j-1]) % 1000000007
    
    answer = ways[n-1][m-1]  
    return answer