#https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    result = [i for i in arr if i % divisor == 0]
    if result:
        return sorted(result)
    else:
        return [-1]
'''
다른 사람 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
list_a or list_b
일때 list_a 가 거짓이면 list_b가 호출

내가 if result 했던 개념으로 똑같이 하면 되네 배워갑니다

'''
