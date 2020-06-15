#https://programmers.co.kr/learn/courses/30/lessons/12926
import string
def solution(s, n):
    lower_aplpa = string.ascii_lowercase*2
    upper_aplpa = string.ascii_uppercase*2
    answer =''
    for i in s:
        if i in lower_aplpa:
            answer += lower_aplpa[lower_aplpa.index(i)+n]
        elif i in upper_aplpa:
            answer += upper_aplpa[upper_aplpa.index(i)+n]
        else:
            answer+=' '
    return answer
'''
ord 아스키 코드 값 반환
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
'''
