#https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    number_list='1234567890'
    if len(s)==4 or len(s)==6:
        for i in s:
            if i not in number_list:
                return False
        return True
    else:
        return False
'''
다른 사람 코드
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
isdigit() -> 숫자인지 판단하는 함수
isalpha() -> 문자인지 판단하는 함수
len(s) in (4,6) 좋네
'''
