#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    d = {}
    for a in participant:
        d[a]= d.get(a,0)+1
    for a in completion:
        d[a]-=1
    dnf= [k for k,v in d.items() if v>0]
    answer = dnf[0]
    return answer
