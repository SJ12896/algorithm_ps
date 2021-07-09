# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    
    last_chr = ''
    word_dict = dict()
    for w in range(len(words)):
        if last_chr and last_chr != words[w][0]:
            answer = [(w % n)+1, (w//n)+1]
            break
        elif last_chr and word_dict.get(words[w]):
            answer = [(w % n)+1, (w//n)+1]
            break
        else:
            last_chr = words[w][-1]
            word_dict[words[w]] = word_dict.setdefault(words[w], 0) + 1
    else:
        answer = [0, 0]

    return answer