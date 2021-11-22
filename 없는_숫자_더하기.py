# https://programmers.co.kr/learn/courses/30/lessons/
# 뺄셈도 sum으로 현재 가진값 다 더해서 하면 되는 문제였다.

def solution(numbers):
    answer = sum(range(1, 10))
    for n in numbers:
        answer -= n
    return answer