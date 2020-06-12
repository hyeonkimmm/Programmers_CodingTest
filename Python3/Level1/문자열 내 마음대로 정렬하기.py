#https://programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    return sorted(sorted(strings),key=lambda x:x[n])
'''
lambda 사용 - 이차원 배열같은데서 활용하기 쉬움 하나씩 다 돌려야하는거
'''
