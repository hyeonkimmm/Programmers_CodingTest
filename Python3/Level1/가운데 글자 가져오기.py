#https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s)%2==0:
        return s[len(s)//2-1]+s[len(s)//2]
    else:
        return s[len(s)//2]
'''
다른 사람 풀이
def string_middle(str):
    # 함수를 완성하세요
    return str[(len(str)-1)//2:len(str)//2+1]

이렇게도 할수 있겠구나 똑똑하군..
그리고 짝,홀 따질 때 if 사용할때 if X%2 가 0아님 1이니까 굳이 == 0 or ==1 안하고
if len(s)%2 :
    # 홀수파트
else:
    # 짝수파트
'''
