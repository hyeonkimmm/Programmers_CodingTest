#https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0
    while(num!=1):
        if answer ==500:
            return -1
        if num%2:
            num=num*3+1
        else:
            num/=2
        answer+=1
    return answer
'''
이게 훨씬 더 깔끔해 보인다.
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
'''
