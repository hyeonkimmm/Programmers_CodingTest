#https://programmers.co.kr/learn/courses/30/lessons/42840
# 내 풀이 
def solution(answers):
    mathfail1 =[1,2,3,4,5] #5번 마다 반복
    mathfail2 =[2,1,2,3,2,4,2,5] #8번 마다 반복
    mathfail3 =[3,3,1,1,2,2,4,4,5,5] # 10번 마다 반복
    correct=[0,0,0]
    answer = []
    for i, v in enumerate(answers):
        # i 번째 문제를 각각의 len(mathfail)로 나눌때의 나머지의 값과 비교
        value1 = i%5
        value2 = i%8
        value3 = i%10
        if v == mathfail1[value1]:
            correct[0]+=1
        if v == mathfail2[value2]:
            correct[1]+=1
        if v == mathfail3[value3]:
            correct[2]+=1
    
    for idx,s in enumerate(correct):
      if s == max(correct):
        answer.append(idx+1)
    return answer

'''
다른 사람 풀이 -- 2차원 배열 + enumberate 중첩 -- 센스있다..
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
    
다른 사람 풀이 -- cycle 활용 --음..
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
'''
