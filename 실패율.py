# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    arrive = [0 for _ in range(N+1)]
    notClear = [0 for _ in range(N+1)]
    
    for s in stages:
        for i in range(s):
            arrive[i] += 1
        notClear[s-1] += 1
    
    temp = []
    for i in range(N):
        if (arrive[i] != 0):
            temp.append([i, (notClear[i] / arrive[i])])
        else:
            temp.append([i, 0])
    temp.sort(key=lambda x : (-x[1], x[0]))
    for x, y in temp:
        answer.append(x+1)
    return answer