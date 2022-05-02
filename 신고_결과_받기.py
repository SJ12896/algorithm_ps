# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

def solution(id_list, report, k):
    answer = []
    dictionary = {}
    total = {}
    
    for repo in report:
        user, user2 = repo.split()
        dictionary[user] = dictionary.get(user, {})
        num = dictionary.get(user).get(user2, 0)
        if num == 0:
            dictionary[user][user2] = num + 1
            total[user2] = total.get(user2, 0) + 1   
    
    for id in id_list:
        answer.append(0)
        for key in dictionary.get(id, {}).keys():
            if (total.get(key, 0) >= k):
                answer[-1] += 1
    return answer