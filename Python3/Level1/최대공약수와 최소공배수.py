#https://programmers.co.kr/learn/courses/30/lessons/12940

from math import gcd
def lcm(x,y):
    return x*y//gcd(x,y)
def solution(n, m):
    return [gcd(n,m),lcm(n,m)]
'''
다른 사람의 풀이
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
    
'''
