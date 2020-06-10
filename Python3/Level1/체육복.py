#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n,lost,reserve):
    a =sorted(list(set(lost)-set(reserve)))
    b =sorted(list(set(reserve)-set(lost)))
    # 중복제거
    sum = 0
    answer = 0
    for i in a:
        if i-1 in b:
            sum+=1
            b= b[b.index(i-1)+1:]
        elif i+1 in b:
            sum+=1
            b = b[b.index(i+1)+1:]
    answer=n-len(a)+sum
    return answer
'''
다른사람 풀이 마땅하게 특출난건 못봤다
  _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    중복제거 할때 이건 나쁘지 않은 것 같음.
    
'''
