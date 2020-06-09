#https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    for i in s:
        a = i.split(',')
        for j in a:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
