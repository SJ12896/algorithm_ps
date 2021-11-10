# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# 제출 후 다른 사람들 풀이를 본 게 도움이 됐다. 정규식 사용하는 건 생각하지도 못했다. 또는 while문을 사용해 '..'을 '.'으로 바꾸는 것도

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    available = [ord('-'), ord('_')]
    check = False
    for n in range(len(new_id)):
        if ord('0') <= ord(new_id[n]) <= ord('9') or ord('a') <= ord(new_id[n]) <= ord('z'):
            answer += new_id[n]
            check = False
        elif ord(new_id[n]) in available:
            answer += new_id[n]
            check = False
        elif ord(new_id[n]) == ord('.'):
            if not check:
                answer += new_id[n]
                check = True
    if answer and answer[0] == '.':
        answer = answer[1:]
    if not answer:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    if answer and answer[len(answer)-1] == '.':
        answer = answer[:len(answer)-1]
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
        
    return answer