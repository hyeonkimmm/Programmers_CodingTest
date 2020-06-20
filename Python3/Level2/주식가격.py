#https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            answer[i]+=1
            if prices[i]>prices[j]:break
    return answer
prices = [1, 2, 3, 2, 3]
print(solution(prices))
'''
o(n2)이라 좀 그렇긴 함..
일단 enumerate랑 list.append()는 효율성에서 떨어진다는 것을 알 수 있었음
'''
