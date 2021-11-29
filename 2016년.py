# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    cnt = b
    for i in range(1, a):
        cnt += days[i]
    answer = date[cnt % 7]
    return answer