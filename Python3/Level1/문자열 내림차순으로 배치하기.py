#https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    return ''.join((sorted(s,reverse=True)))
'''
내림차순은 reverse하면 되고, 대문자는 자동으로 소문자보다 뒤로감
join 사용하면 시퀀스데이터를 str 형태로 붙일 수 있음
' '.join((sorted(s,reverse=True))) 한 칸씩 띄워줌
'-'.join((sorted(s,reverse=True))) -마크로 구분
'\n'.join((sorted(s,reverse=True))) 한줄당 하나씩
'''
