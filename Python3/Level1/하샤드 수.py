#https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    return False if x%sum([int(i) for i in str(x)]) else True
