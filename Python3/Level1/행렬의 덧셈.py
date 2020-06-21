#https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
'''
다른 사람의 풀이
return [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
zip 을 활용하여 하나씩 빼낼 수 있다
'''
