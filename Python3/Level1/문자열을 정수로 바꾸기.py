#https://programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    return int(s)
'''
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result
python과 다르게 풀때 생각해 볼 만한듯.
부호를 정해야 하기 때문에 뒤부터 풀어 준 듯
'''
