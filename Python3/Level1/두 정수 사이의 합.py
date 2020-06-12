#https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    if a==b:
        return a
    elif a>b:
        return sum([b+i for i in range(a-b+1)])
    else:
        return sum([a+i for i in range(b-a+1)])
 '''
 다른 사람 풀이
 def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))
range쓰면 되는구나..!

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2
 수학공식
 abs 는 절대값
 '''
