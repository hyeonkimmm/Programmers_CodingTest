#https://programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    sieve = [True]*(n+1)
    m =int(n**0.5)
    for i in range(2,m+1):
        if sieve[i]==True:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    return len([i for i in range(2,n+1) if sieve[i]==True])
'''
에라토스테네스의 체
기본 개념 - > 최대 약수 구한 이후 나중에 배수들 빼주면 됨
다른 사람의 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
파이썬스럽게 잘 푼 것 같다
set을 활용해서 중복 제거를 한 모습.
'''
