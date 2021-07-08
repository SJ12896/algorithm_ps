# https://programmers.co.kr/learn/courses/30/lessons/64061
# 계속 테스트케이스가 전부 틀려서 대체 어디가 틀렸는지 계속 고민했는데 board 자체를 잘못 보고있었다. 인형뽑을 때 열 기준으로 내려가는데 계속 행을 뽑고 있었다. 문제를 제대로 읽자.


def solution(board, moves):
    answer = 0
    basket = []
    check = 0
    for move in moves:
        for doll in range(len(board)):
            if board[doll][move-1]:
                basket.append(board[doll][move-1])
                board[doll][move-1] = 0
                break
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            answer += 2
            basket.pop()
            basket.pop()
    return answer