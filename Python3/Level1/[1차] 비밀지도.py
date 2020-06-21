#https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = list(map(lambda a,b: a|b,arr1,arr2))
    for i,v in enumerate(answer):
        answer[i]=(str(bin(v)))[2:].replace('1','#').replace('0',' ')
        if len(answer[i])<n:
            answer[i] = ' '*(n-len(answer[i]))+answer[i]
    return answer
'''
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
풀이 개념은 비슷한데 zip을 활용한거랑, rjust를 활용한 센스가 좋았다고 생각한다.
'''
