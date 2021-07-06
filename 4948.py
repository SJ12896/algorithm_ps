# https://www.acmicpc.net/problem/4948
# 에라토스테네스의 체를 사용했다.

p_num = [1] * (123457*2)
p_num[0], p_num[1] = 0, 0

for i in range(2, 123457):
    if p_num[i]:
        for j in range(2*i, 123457*2, i):
            p_num[j] = 0

while True:
    n = int(input())
    temp = 0
    if not n:
        break
    for i in range(n+1, 2*n+1):
        if p_num[i]:
            temp += 1
    print(temp)
