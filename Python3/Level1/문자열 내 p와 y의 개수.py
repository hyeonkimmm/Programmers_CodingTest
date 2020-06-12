#https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    p,y=0,0
    for i in s:
        if i=='p' or i=='P':
            p+=1
            continue
        elif i=='y'or i=='Y':
            y+=1
            continue
    return True if p==y else False
'''
다른 사람의 코드
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
lower()로 소문자 만들고 count()로 숫자 세는 코드!!!
upper()는 대문자 만들 수 있음.

from collections import Counter
def numPY(s):
    # 함수를 완성하세요
    c = Counter(s.lower())
    return c['y'] == c['p'] 
Counter 사용 가능!
'''
