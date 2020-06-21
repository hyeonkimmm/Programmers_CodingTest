#https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    a = s.split(' ')
    answer=[]
    s=''
    for b in a:
        for i in range(len(b)):
            s+=b[i].upper() if i%2==0 else b[i].lower()
        answer.append(s)
        s=''
    return ' '.join(answer)
'''
다른 사람의 플이
return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

'''
