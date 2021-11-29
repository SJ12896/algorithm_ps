# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    data = 0
    for r in range(1, count+1):
        data += price * r
    
    return 0 if money-data >= 0 else abs(money-data)