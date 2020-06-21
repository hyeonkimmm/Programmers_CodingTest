#https://programmers.co.kr/learn/courses/30/lessons/12937
def solution(num):
    return "Odd" if num%2 else "Even"
'''
다른 사람의 풀이
return ["Even", "Odd"][num & 1]
비트 연산을 통한 풀이
'''
