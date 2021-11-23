# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for a in range(len(absolutes)):
        answer = answer + absolutes[a] if signs[a] else answer - absolutes[a]
    return answer