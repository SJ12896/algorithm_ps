N, X = map(int, input().split())

days = list(map(int, input().split()))

temp = sum(days[0:X])
result = temp
cnt = 1

for n in range(X, N):
    temp -= days[n-X]
    temp += days[n]
    if temp > result:
        result = temp
        cnt = 1
    elif result == temp:
        cnt += 1
    
if result == 0: print('SAD')
else: 
    print(result)
    print(cnt)