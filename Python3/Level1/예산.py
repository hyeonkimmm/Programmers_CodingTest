#https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d = sorted(d)
    answer = 0
    for i in d:
        if budget-i<0:
            return answer
        else:
            budget-=i
            answer+=1
    return answer
'''

'''
