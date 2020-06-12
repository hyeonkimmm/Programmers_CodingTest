#https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==len(arr)-1:
            answer.append(arr[i])
        elif arr[i]==arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    return answer
'''
Python List IndexError : list index out of range
리스트 활용시 자주 발생하게 되는 에러인데, 나는 i값이 마지막인지 검사하여 처리하였는데,
다른 사람의 풀이중

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
이런식으로 a[-1:]로 슬라이싱을 활용하는데,
슬라이싱은 인덱스 에러가 발생하지 않음 앞으로 많이 자주 활용 할 수 있겠다.

'''
