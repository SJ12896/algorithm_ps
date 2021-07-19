# https://programmers.co.kr/learn/courses/30/lessons/77484
# 다시 알고리즘 좀 열심히 해야지...

def solution(lottos, win_nums):
    answer = []
    cnt_0 = 0
    
    for l in lottos:
        if not l:
            cnt_0 += 1
    
    cnt_cor = len(set(win_nums) - set(lottos)) + 1
    low = cnt_cor
    low = low if low < 7 else 6
    high = low-cnt_0 if low-cnt_0 >= 1 else 1
    
    answer = [high, low]
    return answer