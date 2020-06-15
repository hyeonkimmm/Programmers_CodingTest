#https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(num):
    return num + sum([i for i in range(1, (num //2) + 1) if num % i == 0])
