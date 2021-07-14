# https://programmers.co.kr/learn/courses/30/lessons/12977
# 알고리즘 좀 쉬었다고 문제들이 이렇게 어렵게 느껴질 수 있나? 결국 쉬운 문제를 찾아 헤매다 풀었다 ...

from itertools import combinations

def solution(nums):
    answer = 0

    sosu = [1] * 3000
    sosu[0], sosu[1]  = 0, 0
    for s in range(2, len(sosu)):
        if sosu[s] == 1:
            for i in range(2*s, len(sosu), s):
                sosu[i] = 0
    
    for com in list(combinations(nums, 3)):
        if sosu[sum(com)]:
            answer += 1

    return answer