# https://programmers.co.kr/learn/courses/30/lessons/81301
# dictionary까지 생각했는데 replace 메소드를 완전 잊고 있었다. replace를 사용하면 간편하게 바꿀 수 있다.

def solution(s):
    answer = ''
    nums = {'zero' : '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    temp = ''
    for c in s:
        if ord('0') <= ord(c) <= ord('9'):
            answer += c
        else:
            temp += c
            if temp in nums.keys():
                answer += nums[temp]
                temp = ''
    answer = int(answer)
    return answer