# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
# min을 사용하면 훨씬 간단하게 표현할 수 있었다.

def solution(nums):
    nums_set = set(nums)
    answer = len(nums_set) if len(nums_set) <= len(nums)// 2 else len(nums)// 2
    return answer