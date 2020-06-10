#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for idx,val in enumerate(commands):
        a = sorted(array[val[0]-1:val[1]])
        answer.append(a[val[2]-1])
    return answer
'''
다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
lambda를 활용해서 2차원 배열인 commands에하나씩 읽어 오면서 list로 저장 후 return

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
    
나랑 비슷한 풀이
2차원 배열 for문 했을 때 저렇게 command 로 한꺼번에 값 저장 할 수 있는것을 배웠다
'''
