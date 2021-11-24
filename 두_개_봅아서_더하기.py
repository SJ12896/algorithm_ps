# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set()
    for n in range(0, len(numbers)-1):
        for n2 in range(n+1, len(numbers)):
            answer.add(numbers[n]+numbers[n2])
    return sorted(list(answer))