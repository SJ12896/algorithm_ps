# 임의 위치부터 k개 연속 먹으면 할인된 가격
# 위에 참여하고 쿠폰이 있으면 쿠폰 초밥 하나 무료. 없으면 만들어줌
# 가능한 다양한 종류로 먹기
# 접시 수 N / 초밥 가짓수d / 연속해서 먹는 접시 수 k / 쿠폰 번호 c


N, d, k, c = map(int, input().split())
sushi = []
temp, result = 0, 0

for n in range(N):
    sushi.append(int(input()))

for i in range(N):
    set_data = set([c])
    if i+k < N:
        set_data.update(sushi[i:i+k])
    else:
        set_data.update(sushi[i:N])
        set_data.update(sushi[0:i+k-N])
    temp = len(set_data)
    if temp > result: result = temp
print(result)