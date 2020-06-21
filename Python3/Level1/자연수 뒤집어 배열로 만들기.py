#https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    return [int(i) for i in str(n)[::-1]]
'''
다른 사람의 풀이
return list(map(int, reversed(str(n))))
'''
