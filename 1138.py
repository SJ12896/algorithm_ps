# 백준 1138 https://www.acmicpc.net/problem/1138
# 오랜만에 풀었더니 상당히 이상하게 푼 것 같다.

N = int(input())

people = list(map(int, input().split()))
result = [0] * N
for n in range(N):
    temp = 0
    for m in range(N):
        if not result[m]:
            temp += 1
            if not people[n]:
                result[m] = n+1
                break
        if temp == people[n] and not result[m+1]:
            result[m+1] = n+1
            break

print(*result)