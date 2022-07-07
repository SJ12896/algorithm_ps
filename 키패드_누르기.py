# https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 좀 더 쉽게 풀 방법이 없을까 고민했는데 이 아이디어로 푸는게 맞는 방향이었다...

def solution(numbers, hand):
    answer = ''
    dict = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2] , '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left, right = '*', '#'
    
    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            left = num
        elif num in (3, 6, 9):
            answer += 'R'
            right = num
        else:
            target_loc = dict.get(num)
            left_loc = dict.get(left)
            right_loc = dict.get(right)
            temp_left = abs(target_loc[0] - left_loc[0]) + abs(target_loc[1] - left_loc[1])
            temp_right = abs(target_loc[0] - right_loc[0]) + abs(target_loc[1] - right_loc[1])
            
            if temp_left > temp_right:
                answer += 'R'
                right = num
            elif temp_left < temp_right:
                answer += 'L'
                left = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
    return answer