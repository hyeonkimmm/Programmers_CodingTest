#https://programmers.co.kr/learn/courses/30/lessons/42586
import math
def solution(progresses, speeds):
    answer =[]
    progresses = [math.ceil(100-a)//b for a,b in zip(progresses,speeds)]
    print(progresses)
    front=0
    for i in range(len(progresses)):
        if progresses[front]< progresses[i]:
            answer.append(i-front)
            front=i
    answer.append(len(progresses)-front)
    return answer
