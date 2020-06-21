#https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    del arr[arr.index(min(arr))]
    return arr if len(arr)>0 else [-1]
'''
다른 사람의 풀이
return [i for i in mylist if i > min(mylist)]
'''
